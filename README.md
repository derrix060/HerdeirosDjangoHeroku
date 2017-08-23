# OngHerdeiros - Backend

This is a service to get itens needed by Ong Herdeiros and all the events.

## Events
To see all the events, make a GET request to this endpoint: https://dry-anchorage-70819.herokuapp.com/api/eventos/

example of return:
```json
[
  {
    "titulo_text": "Inaugura\u00e7\u00e3o do Centro de Refer\u00eancia da Mulher do Cap\u00e3o Redondo", 
    "date_date": "24/08/2017 - 15:36", 
    "local_text": "R. Bandeira Paulista, 123", 
    "description_text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer maximus laoreet nisi, non accumsan erat dictum vitae. Ut consequat imperdiet.", 
    "image_src_text": "https://static.wixstatic.com/media/7eb1a2_dc3d3be8fb0c4e90afb4c411753cbd37~mv2.jpg_256"
   }, 
   {
    "titulo_text": "Lorem Ipsum", 
    "date_date": "30/08/2017 - 18:00", 
    "local_text": "R qualquer 123", 
    "description_text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec efficitur dolor ac erat ultricies, sit amet volutpat urna pulvinar. Cras.", 
    "image_src_text": "https://static.wixstatic.com/media/7eb1a2_0842c294b6584adeb415183537c97e58~mv2.jpg_128"
    }
]
```

## Itens needed
To see all the itens needed, make a GET request to this endpoint: https://dry-anchorage-70819.herokuapp.com/api/itens/

example of return:
```json
[
  {
    "name_text": "Geladeira", 
    "image_src_text": "http://electrolux.vteximg.com.br/arquivos/ids/180294-260-260/Refrigerador-French-Door-579-L-Inox-DM8", 
    "amount": 1
  }, 
  {
    "name_text": "Carro", 
    "image_src_text": "http://soicones.com/icones/automoveis/carro.png", 
    "amount": 1
  }, 
  {
    "name_text": "Camera", 
    "image_src_text": "", 
    "amount": 1
  }
]
```
