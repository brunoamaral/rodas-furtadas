# Running with Docker

```bash
git clone git@github.com:brunoamaral/rodas-furtadas.git && cd rodas-furtadas
cp example.env
read -p "Please edit the .env file and press any key ..."
sudo docker-compose up -d --build
sudo docker exec -it django ./manage.py migrate
open http://localhost:8000/ 
open http://localhost:8000/admin
```