<template>
  <div class="container">
    <button
      ref="record"
      type="button"
      class="btn btn-danger"
      v-on:click="onRecord"
      :disabled="recording"
    >
      Record
    </button>
    <button
      ref="stopRecord"
      type="button"
      class="btn btn-secondary ml-2"
      v-on:click="onStop"
      :disabled="!recording"
    >
      Stop
    </button>
    <audio class="ml-5" controls ref="recordedAudio"></audio>
  </div>
</template>

<script>
export default {
  name: "Record",
  data() {
    return {
      audioChunks: [],
      recording: false,
    };
  },
  methods: {
    handlerFunction(stream) {
      this.rec = new MediaRecorder(stream);
      this.rec.ondataavailable = (e) => {
        this.audioChunks.push(e.data);
        if (this.rec.state == "inactive") {
          let blob = new Blob(this.audioChunks, { type: "audio/mpeg-3" });
          this.$refs.recordedAudio.src = URL.createObjectURL(blob);
          this.$refs.recordedAudio.controls = true;
          this.$refs.recordedAudio.autoplay = true;
          this.sendData(blob);
        }
      };
      this.rec.onstop = (e) => {
        const blob = new Blob(this.audioChunks, { type: "audio/ogg; codecs=opus" });
        this.audioChunks = [];
        const audioURL = this.window.URL.createObjectURL(blob);
        this.$refs.recordedAudio.src = audioURL;
      };
    },
    onRecord(e) {
      this.recording = true;
      this.rec.start();
    },
    onStop(e) {
      this.recording = false;
      this.rec.stop();
    },
    sendData(blob) {
      // pass
    },
  },
  created() {
    this.navigator.mediaDevices
      .getUserMedia({ audio: true })
      .then(this.handlerFunction);
  },
};
</script>
