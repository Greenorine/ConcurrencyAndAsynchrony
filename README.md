# ConcurrencyAndAsynchrony
## При синхронной обработке  
Время выполнения:  
![pycharm64_xpYV9VSBSz](https://user-images.githubusercontent.com/41028671/143774896-c531ecb4-7c6e-4e1a-ad33-7ee2d5b86c31.png)  

## При 5 воркерах  
Время выполнения:  
![pycharm64_bvk3HOFVJ6](https://user-images.githubusercontent.com/41028671/143774652-80f1371a-937f-4b23-9eff-a891c43049f0.png)  
Загруженность:  
![Taskmgr_26u9B1jrwZ](https://user-images.githubusercontent.com/41028671/143774664-27766b11-c029-4185-92e6-6755508ad8de.png)  

## При 10 воркерах  
Время выполнения:  
![pycharm64_CvK4i34uZg](https://user-images.githubusercontent.com/41028671/143774672-98b84f32-d3fc-47aa-9210-c78dbe8bedc6.png)  
Загруженность:  
![Taskmgr_wANxqE4U1y](https://user-images.githubusercontent.com/41028671/143774675-eb709c1c-a936-482b-8ab6-fca8bcea26db.png)  

## При 100 воркерах  
Время выполнения:  
![pycharm64_P0pxeK5VZ8](https://user-images.githubusercontent.com/41028671/143774689-65fd2f06-704e-47bd-b7fa-98bb70d8addf.png)  
Загруженность:  
![Taskmgr_veA03XulrQ](https://user-images.githubusercontent.com/41028671/143774694-c50f9ed7-add3-431a-b15f-308ef62735cd.png)  

## Размышления  
Можно заметить, что мощность, которую задействует процессор, растёт по мере роста количества воркеров, как и загрузка сети, поскольку количество обращений увеличивается ввиду большего количества обрабатываемых воркеров.
