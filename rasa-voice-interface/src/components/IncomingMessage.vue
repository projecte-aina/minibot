<template>
	<transition name="slide-fade" mode="out-in" :duration="{ enter: 500, leave: 500 }">
		<div :key="getCurrentIncomingMessage.text" class="incoming-msg">
			<WaitingResponse v-if="waitForResponse || incomeMessage.length === 0"/>
			<div v-else>
					<div v-if="getCurrentIncomingMessage.text" class="message-content float-left">
						<vue-markdown :source="getCurrentIncomingMessage.text"></vue-markdown>
					</div>
					<!-- <dir class="media-content">
							<ImageCustom :srcUrl="'https://static.boredpanda.com/blog/wp-content/uploads/2018/04/5acb63d83493f__700-png.jpg'"/>
					</dir> -->
					<!-- <dir class="media-content">
							<QuickReplies :quickReplies="[{title: 'hello', payload: 'hello'},{title: 'good', payload: 'good'}]"/>
					</dir> -->
					<div v-if="getCurrentIncomingMessage.attachment" class="media-content">

						<dir v-if="getCurrentIncomingMessage.attachment.type==='image'">
							<ImageCustom :srcUrl="getCurrentIncomingMessage.attachment.payload.src"/>
						</dir>

						<dir v-if="getCurrentIncomingMessage.attachment.type==='video'">
							<VideoPlayer :srcUrl="getCurrentIncomingMessage.attachment.payload.src"/>
						</dir>

						<dir v-if="getCurrentIncomingMessage.attachment.type==='template' && getCurrentIncomingMessage.attachment.payload==='generic'">
							<p>{{ getCurrentIncomingMessage.text }}</p>
						</dir>
					</div>

					<div v-if="getCurrentIncomingMessage.quick_replies" class="qr-content">
						<QuickReplies :quickReplies="getCurrentIncomingMessage.quick_replies"/>
					</div>
				</div>
			</div>
	</transition>
</template>

<script>
import { mapGetters, mapState } from 'vuex';
import VueMarkdown from 'vue-markdown';
import ImageCustom from './ImageCustom.vue';
import VideoPlayer from './VideoPlayer.vue';
import QuickReplies from './QuickReplies.vue';
import WaitingResponse from './WaitingResponse';

export default {
	name: 'IncomingMessage',
	components: {
		ImageCustom,
		VideoPlayer,
		QuickReplies,
		WaitingResponse,
		VueMarkdown
	},
	computed: {
		...mapGetters(['waitForResponse', 'getCurrentIncomingMessage']),
		...mapState(['incomeMessage'])
	},
};
</script>

<style lang="scss">
#app .incoming-msg {
	min-height: 50vh;
	max-width: 80%;
	text-align: left;
	z-index: 20;
	.message-content {
		text-align: left;
		display: inline-block;
		width: 100%;
		margin: 0 0 0 0;
		background: transparent;
		margin-left: 10%;
		p {
			min-width: 300px;
      max-height: 400px;
      overflow-y: auto;
			display: inline-block;
			color: white;
			font-size: 30px;
			margin: 0;
			padding: 8px 15px;
			word-break: break-word;
			line-height: 1.2em;
      scrollbar-width: thin;
      scrollbar-color: transparent #fff;

      &::-webkit-scrollbar {
        width: 10px;
      }

      &::-webkit-scrollbar-track {
        -webkit-border-radius: 10px;
        border-radius: 10px;
      }


      &::-webkit-scrollbar-thumb {
        -webkit-border-radius: 8px;
        border-radius: 8px;
        background: transparent;
        border: 1px solid #fff;
      }
		}
	}
	.media-content {
		display: inline-block;
		max-width: 600px;
		margin-left: 10%;
	}
	.qr-content {
		display: inline-block;
		max-width: 100%;
		// min-width: 50%;
		margin: 20px;
		margin-left: 15%;
		background: transparent;
	}
  //@media only screen and (max-height: 800px) {
  //  .message-content {
  //    p {
  //      max-height: 248px;
  //      font-size: 20px;
  //    }
  //  }
  //}
	@media only screen and (max-width: 600px) {
		width: 90%;
		max-width: 90%;
		.message-content {
			margin: 0;
			width: 100%;
			p {
        max-height: 248px;
				font-size: 24px;
			}
		}
		.media-content {
			margin: 0;
			width: 100%;
		}
		.qr-content {
			margin: 0;
			width: 100%;
		}
	}
}
</style>
