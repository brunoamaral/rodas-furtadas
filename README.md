# Discussion and updates

[Fórum Ciclismo](https://www.forumciclismo.net/index.php?threads/rodas-furtadas-o-registo-de-bicicletas-roubadas.21169/#post-444967)


# Running with Docker

```bash
git clone git@github.com:brunoamaral/rodas-furtadas.git && cd rodas-furtadas
cp example.env
read -p "Please edit the .env file and press any key ..."
sudo docker-compose up -d --build
sudo docker exec -it django ./manage.py migrate
sudo docker exec -it django ./manage.py createsuperuser
# remember to configure your static root
sudo docker exec -it django ./manage.py collectstatic
open http://localhost:8000/ 
open http://localhost:8000/admin
```
