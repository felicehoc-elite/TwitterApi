# TwitterApiDBFactory

 

 

 

 

 

 

 

 

Rapport de Projet : 

Extraction, analyse et structuration de Tweets 

 

 

 

 

 

 

 

 

 

Réalisée par : 

Haithem KAHIL 

Nasma BRAHMI 

 

 

 

 

 

 

 

Introduction : 

De nos jours, les réseaux sociaux tiennent une place majeure dans la diffusion de l’actualité, et contribuent au développement d’une nouvelle forme d’expression. 

L’étude de ces réseaux peut donc apporter de nombreuses informations à la fois sur la mise en place d’une pensée collective mais également sur des messages plus singuliers et ponctuels. 

Twitter est l’un des réseaux les plus en vogues depuis quelques années déjà, c’est une véritable source d’informations qui peut apporter de nouvelles connaissances à de nombreuses études. 

En effet, une API a été mise en place par Twitter, permettant d’interroger sa base de données et de récupérer des informations concernant les tweets. Deux méthodes principales sont utilisées dans ce cadre, l’API REST qui permet de faire des requêtes sur les tweets déjà présents dans la base de données, et de l’API STREAMING qui permet d’accéder au flux de tweets en temps réel de manière continue. 

 

Conception du schéma de données : 

1- Accéder à l’API Twitter : 

La première étape consiste à créer un compte développeur sur https://developer.twitter.com/  

et faire approuver son cas d’utilisation. 

Une fois le compte approuvé, la deuxième étape est de créer un projet et connecter une application de développeur associée, qui nous a fournis un ensemble de clés API et jetons d’accès. 

 
![twitter](https://user-images.githubusercontent.com/72985793/102413055-a6ec3480-3ff4-11eb-96fb-b6731b2b8474.PNG) 

 

2- Récupération des Tweets : 

Pour accéder aux données via l’API REST, nous avons créé une requête HTTP de type GET avec le point de terminaison : l’URL : https://api.twitter.com/2/tweets en précisant les champs souhaités. 

La réponse à cette requête est de format JSON. 


![JSON](https://user-images.githubusercontent.com/72985793/102413056-a8b5f800-3ff4-11eb-9391-8531b10bd4ea.PNG)


3- Conception de la base de données : 

En analysant les tweets récupérés sous format JSON, nous avons modélisé une base de données relationnelle qui se présente comme suit : 

 
![diagramme_Twitter](https://user-images.githubusercontent.com/72985793/102413061-aa7fbb80-3ff4-11eb-83a9-696e9489ca3c.PNG) 

 



 

 
