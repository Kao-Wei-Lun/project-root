<template>
  <div class="home">
    <!-- 首頁主視覺區 (Hero Section) -->
    <!-- <section class="hero">
      <h1>歡迎來到 XX 工作室</h1>
      <p>我們專注於數字易經、療癒占卜及神秘商品，幫助您找到心靈的平衡與生活的智慧。</p>
    </section> -->

    <!-- 服務項目預覽區 -->
    <section class="services">
      <h2>服務項目</h2>
      <div class="service-list">
        <div v-for="service in services" :key="service.id" class="service-card">
          <img :src="service.image" :alt="service.name" />
          <h3>{{ service.name }}</h3>
          <p>{{ service.description }}</p>
          <!-- 根據 service.id 從 mapping 中取出對應的路由 -->
          <router-link :to="serviceRoutes[service.id]">了解更多</router-link>
        </div>
      </div>
    </section>

    <!-- 系統推薦區 -->
    <!-- <section class="recommendations">
      <h2>系統推薦</h2>
      <p>根據最新的需求分析，我們推薦您體驗療癒與服務項目。</p>
    </section> -->

    <!-- 諮詢師介紹預覽 -->
    <section class="consultants">
      <h2>諮詢師介紹</h2>
      <p>我們的專業團隊將協助您解答各種疑問。</p>
      <router-link to="/consultant">查看更多</router-link>
    </section>

    <!-- 客戶回饋分享預覽 -->
    <section class="feedback">
      <h2>回饋分享</h2>
      <p>看看其他客戶的體驗與回饋，了解我們服務的效果。</p>
      <router-link to="/feedback">查看更多回饋</router-link>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      // 服務項目的靜態資料（日後可改為從 API 取得）
      services: [
        {
          id: 'digital',
          name: '數字易經諮詢',
          description: '涵蓋人生藍圖、事業、家庭關係、存摺運用、整體諮詢',
          image: '/assets/test.png'
        },
        {
          id: 'healing',
          name: '療癒與服務',
          description: '號碼調整、獨角獸靈氣、天使靈氣、富裕靈氣、寵物溝通、寶寶溝通',
          image: '/assets/test.png'
        },
        {
          id: 'divination',
          name: '牌卡占卜',
          description: '獨角獸牌卡、雷諾曼牌卡（單題$300、5題$1200）',
          image: '/assets/test.png'
        },
        {
          id: 'product',
          name: '商品販售',
          description: '魔法蠟燭、魔法噴霧',
          image: '/assets/test.png'
        }
      ],
      // 將服務 id 與獨立路由做對應
      serviceRoutes: {
        digital: '/service/digital',
        healing: '/service/healing',
        divination: '/service/divination',
        product: '/service/product'
      }
    }
  }
}
</script>

<style scoped>
.home {
  padding: 20px;
}

/* 主視覺區 */
.hero {
  text-align: center;
  padding: 40px 20px;
  background: #f5f5f5;
  margin-bottom: 40px;
}

/* 服務項目預覽區 */
.services {
  margin-bottom: 40px;
}

.service-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
}

.service-card {
  border: 1px solid #ddd;
  padding: 15px;
  width: 250px;
  text-align: center;
  border-radius: 8px;
  transition: transform 0.3s;
}

.service-card:hover {
  transform: scale(1.05);
}

.service-card img {
  width: 100%;
  height: auto;
  border-radius: 4px;
}

/* 其他區塊樣式 */
.recommendations,
.consultants,
.feedback {
  text-align: center;
  margin-bottom: 40px;
}

.recommendations p,
.consultants p,
.feedback p {
  margin-bottom: 15px;
}
</style>
