<template>
  <div>
    <div class="d-flex justify-content-center">
      <img src="@/assets/community.png" alt="" id="community_img">
    </div>

    <div class="d-flex justify-content-md-end">
      <button type="button" class="btn" id="createBoardBtn" @click="onCreate" >글 작성하기</button>
    </div>
    <div id="freeBoardTable" class="container">
      <table class="table">
        <thead >
          <tr class="table-secondary">
            <th scope="col">#</th>
            <th scope="col">제목</th>
            <th scope="col">작성자</th>
            <th scope="col">작성 시간</th>
          </tr>
        </thead>
        <BoardTable v-for="review in paginatedData" :key="review.id" :review="review"/>
      </table>

      <div>
        <div class="btn-cover text-center">
          <button :disabled="pageNum === 0" @click="prevPage" class="page-btn btn">
            이전
          </button>
          <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span>
          <button :disabled="pageNum >= pageCount - 1" @click="nextPage" class="page-btn btn">
            다음
          </button>
        </div>
      </div>

    </div>


  </div>
</template>

<script>
import { mapState } from 'vuex'
import BoardTable from '@/components/BoardTable'

export default {
  name: 'FreeBoard',
  components: {
    BoardTable,
  },
  data: function () {
    return {
      pageNum: 0,
    }
  },
  methods: {
    onCreate: function() {
      this.$router.push({name: 'FreeBoardCreate'})
    },
    // 페이지네이션
    nextPage () {
      this.pageNum += 1;
    },
    prevPage () {
      this.pageNum -= 1;
    }
  },


  computed: {
    ...mapState(['review_list']),
    pageCount () {
      let listLeng = this.review_list.length,
          listSize = 10,
          page = Math.floor(listLeng / listSize);
      if (listLeng % listSize > 0) page += 1;
      
      /*
      아니면 page = Math.floor((listLeng - 1) / listSize) + 1;
      이런식으로 if 문 없이 고칠 수도 있다!
      */
      return page;
    },
    paginatedData () {
      const start = this.pageNum * 10,
            end = start + 10;
      return this.review_list.slice(start, end);
    }
  }

}
</script>

<style>
span {
  cursor: pointer;
}

#freeBoardTable {
  width: 1500px;
  height: 400px;
}

#createBoardBtn {
  margin: 20px;
  color: #262223;
  background-color: #DDC6B6;
  font-size: 18px;
  font-weight: bold;
}

#community_img {
  width: 400px;
  height: 150px;
}
</style>