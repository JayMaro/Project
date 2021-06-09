<template>
  <div>
    <h1 class="d-flex justify-content-center" id="freeBoardLogo">Free Board</h1>
    <hr>
    <div id="freeBoardForm" class="content">
      <div class="mb-3">
        <label for="exampleFormControlInput1" class="form-label">제목</label>
        <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="제목" v-model="review.title">
      </div>
      <div class="mb-3">
        <label for="exampleFormControlTextarea1" class="form-label">내용</label>
        <textarea class="form-control" id="exampleFormControlTextarea1" rows="15" placeholder="내용" v-model="review.content"></textarea>
      </div>
    </div>
    <div class="d-flex justify-content-md-end">
      <button class="btn" id="saveBoardBtn" @click="$store.dispatch('createReview', review)">저장</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FreeBoardCreate',

  data: function() {
    return {
      review : {
        title: null,
        content: null,
      }
    }
  }
}
</script>

<style>
#freeBoardForm {
  padding: 20px;
  color: white;
  font-size: 20px;
}

#freeBoardLogo {
  color: white;
  margin: 10px;
}

#saveBoardBtn {
  width: 100px;
  height: 40px;
  margin: 20px;
  background-color: #DDC6B6;
  font-size: 17px;
  font-weight: bold;
}
</style>