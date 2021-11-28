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
Можно заметить, что мощность, которую задействует процессор, растёт по мере роста количества воркеров, как и загрузка сети, поскольку количество обращений увеличивается ввиду большего количества обрабатываемых воркеров. Также, как мы можем заметить, при асинхронной работе задачи время выполнения уменьшается в разы с ростом кол-ва воркеров, чего нельзя сказать о синхронном программировании.  


# CPU Bound  
## При 2 воркерах  
Время выполнения:  
![image](https://user-images.githubusercontent.com/41028671/143776291-1a96e583-6295-4696-8218-e2ec28899209.png)  

Загрузка:  
![image](https://user-images.githubusercontent.com/41028671/143776286-ade77899-2e2c-4718-9fdd-4a861e253319.png)  

## При 4 воркерах  
Время выполнения:  
![image](https://user-images.githubusercontent.com/41028671/143776305-d54f6e55-e855-49e8-b4bc-4c7c5dc4fb48.png)  

Загрузка:  
![image](https://user-images.githubusercontent.com/41028671/143776300-f05dd3fd-2ef4-4ff2-91c1-5d39694998b1.png)  

## При 5 воркерах  
Время выполнения:  
![image](https://user-images.githubusercontent.com/41028671/143776329-30871f43-abcf-40d7-b500-00fa01bb8776.png)  

Загрузка:  
![image](https://user-images.githubusercontent.com/41028671/143776327-31114ad6-d722-40a5-b1fa-b740af960f16.png)  

## При 10 воркерах  
Время выполнения:  
![image](https://user-images.githubusercontent.com/41028671/143776345-97438cc9-924a-4bed-bb9a-8ef70f4645d2.png)  

Загрузка:  
![image](https://user-images.githubusercontent.com/41028671/143776341-d0d99ca6-1637-4ca6-883d-5150fbdbd7dc.png)  

## При 61 воркерах  
Время выполнения:  
![image](https://user-images.githubusercontent.com/41028671/143776368-d22dc082-c292-4b5a-b4ef-7e83cc9ba600.png)

Загрузка:  
![image](https://user-images.githubusercontent.com/41028671/143776356-962ca4ce-4f7b-4eef-9714-249fceae6de8.png)  

## При 100 воркерах  
![image](https://user-images.githubusercontent.com/41028671/143776373-fc152384-ca82-40f0-85ad-79781614a9eb.png)  

## Размышления  
От количества воркеров не зависит время работы, оно абсолютно случайно, так как происходит рандом символов, может быть и 1 секунда, может и 30-60с., также можно заметить что показатели в диспетчере задач практически не меняются, следовательно, они не зависят от кол-ва ворекров в данной задаче.  
