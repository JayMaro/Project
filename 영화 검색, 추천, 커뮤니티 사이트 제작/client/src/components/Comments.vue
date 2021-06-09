<template>
  <div>
    <div class="freeBoardItem p-2" id="commentItem">
      <span>
        {{ comment.content }}
      </span>
      <p class="d-flex justify-content-end m-0">
        작성자 : {{ comment.user['username'] }} ||
        댓글 생성일 : {{ comment['created_at'] }}
      </p>
    </div>
    <div class="d-flex justify-content-end me-3">
      <button class="btn" id="commentDelBtn" @click="OnCommentDel(comment)">댓글 삭제</button>
    </div>
  </div>
</template>

<script>
import {mapState} from 'vuex'
import axios from 'axios'

export default {
  name: 'Comments',
  props: {
    comment : {
      type: Object,
    },
    review_id : {
      type: Number,
    }
  },
  methods: {
    OnCommentDel: function(comment) {
      this.$store.dispatch('setToken')
      axios({
        method: 'delete',
        url: this.server_url + `freeboard/comment/${comment.id}/`,
        headers: this.jwtHeader
      })
      .then(() => {
        this.$store.dispatch('getComments', this.review_id)
        this.$router.push({ name: 'FreeBoardDetail', params: { id: this.review_id }})
      })
      .catch(() => {
        alert('댓글 작성자만 삭제가 가능합니다.')
      })

    }
  },
  computed: {
    ...mapState(['server_url', 'jwtHeader']),
  },

}
</script>

<style>
#commentItem{
  font-size: 17px;
  color: black;
  border-radius: 10px;
}

#commentDelBtn{
  border-color: #DDC6B6;
}
</style>