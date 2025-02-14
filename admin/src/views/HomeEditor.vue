<template>
    <div class="home-editor">
      <h1>首頁內容編輯</h1>
      <div class="editor-wrapper">
        <!-- 編輯區：可以是 Markdown 編輯器或 WYSIWYG 編輯器 -->
        <textarea v-model="content" placeholder="請輸入首頁內容"></textarea>
        <!-- 預覽區：將 Markdown 轉換成 HTML 預覽，這裡僅作簡單示例 -->
        <div class="preview" v-html="compiledContent"></div>
      </div>
      <button @click="handlePublish">發佈</button>
    </div>
  </template>
  
  <script>
  import { ref, computed } from 'vue'
  import { marked } from 'marked'  // 改成命名匯出
  
  export default {
    name: 'HomeEditor',
    setup() {
      const content = ref('');
      const compiledContent = computed(() => marked.parse(content.value));
  
      const handlePublish = async () => {
        try {
          // 呼叫後端 API 更新首頁內容
          await fetch('http://127.0.0.1:8000/api/admin/update-home/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ content: content.value })
          });
          alert('發佈成功！');
        } catch (error) {
          console.error('發佈失敗：', error);
          alert('發佈失敗，請重試。');
        }
      };
  
      return { content, compiledContent, handlePublish }
    }
  }
  </script>
  
  <style scoped>
  .home-editor {
    padding: 20px;
  }
  .editor-wrapper {
    display: flex;
    gap: 1rem;
  }
  textarea {
    width: 50%;
    height: 300px;
    padding: 0.5rem;
  }
  .preview {
    width: 50%;
    height: 300px;
    padding: 0.5rem;
    border: 1px solid #ddd;
    overflow-y: auto;
    background: #fff;
  }
  button {
    margin-top: 1rem;
    padding: 0.5rem 1rem;
  }
  </style>
  