# project-root

#python -m venv env
啟動虛擬環境:
env\Scripts\activate

python manage.py runserver

建立資料庫遷移檔並同步資料庫：
python manage.py makemigrations
python manage.py migrate

建立管理員資訊
python manage.py createsuperuser

# 使用 Vite 建立 Vue3 專案範例
npm init vite@latest frontend -- --template vue
cd frontend
npm install

npm run dev

Failed to resolve import "vue-router" from "src/router/index.js". Does the file exist?
npm install vue-router@4

npm install marked

npm init vite@latest admin -- --template vue
