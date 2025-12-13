#!/bin/bash

echo "🚀 Начинаю установку проекта..."

# # 1. Спросить у пользователя, куда установить проект
read -p "📂 Введите название директории для установки (или '.' для текущей): " TARGET_DIR

if [ "$TARGET_DIR" == "." ]; then
    echo "📌 Устанавливаю проект в текущую директорию..."
    git clone https://github.com/Muhammadaziz-beckend/start-project.git .
else
    echo "📌 Создаю директорию '$TARGET_DIR' и устанавливаю проект туда..."
    mkdir -p "$TARGET_DIR"
    git clone https://github.com/Muhammadaziz-beckend/start-project.git "$TARGET_DIR"
    cd "$TARGET_DIR" || exit
fi

# 2. Создаём виртуальное окружение
echo "🔧 Создаю виртуальное окружение..."
python3 -m venv venv
source venv/bin/activate

# 3. Устанавливаем зависимости
echo "📦 Устанавливаю зависимости..."
pip install --upgrade pip
pip install -r requirements.txt

# 4. Создаем .env
echo "🧩 Создаю .env файл..."
cat > .env <<EOF
SECRET_KEY=dev-secret-key
DEBUG=True
DB_NAME=postgres
DB_USER=postgres
DB_PASS=password
DB_HOST=localhost
DB_PORT=5432
PORT_WEB=8000
EOF

# 5. Миграции
echo "🗄 Выполняю миграции..."
python manage.py makemigrations account
python manage.py makemigrations
python manage.py migrate

# 6. Финал
echo "✅ Установка завершена!"
echo "▶ Чтобы запустить проект:"
echo "source venv/bin/activate && python manage.py runserver"
