mkdir -p ~/.streamlit/

echo “
[general]
email = \”rodelarenas@gmail.com\”
“ > ~/.streamlit/credentials.toml

echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
