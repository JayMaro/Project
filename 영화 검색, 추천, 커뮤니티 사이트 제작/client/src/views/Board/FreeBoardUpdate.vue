<template>
  <div>
    <h1 class="d-flex justify-content-center" id="freeBoardLogo">게시글 수정</h1>
    <hr>
    <div id="freeBoardForm" class="content">
      <div class="mb-3">
        <label for="exampleFormControlInput1" class="form-label">제목</label>
        <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="제목" v-model="new_review.title">
      </div>
      <div class="mb-3">
        <label for="exampleFormControlTextarea1" class="form-label">내용</label>
        <textarea class="form-control" id="exampleFormControlTextarea1" rows="15" placeholder="내용" v-model="new_review.content"></textarea>
      </div>
    </div>
    <div class="d-flex justify-content-md-end">
      <button class="btn" id="saveBoardBtn" @click="$store.dispatch('updateReview', [review.id, new_review])">수정완료</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FreeBoardUpdate',

  data: function() {
    return {
      new_review: {
        title: this.review.title,
        content: this.review.content,
      }
    }
  },
  props: {
    review: {
      type: Object,
    }
  },

}
</script>

<style>

</style>