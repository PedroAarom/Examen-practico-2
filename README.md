# Examen-practico-2

## Sección 1) Configuración del Entorno de Desarrollo

### Crea una EC2 Amazon Linux, con su clave, y configura el puerto 5000 para el flask en el grupo de seguridad, 
### Crea un Cloud9 y con la clave conectate a tu EC2, luego instalate el git sudo yum install git, con git clone, clonate el repositorio

![image](https://github.com/PedroAarom/Examen-practico-2/assets/166650957/f70c1c93-e393-4819-ae2f-b7a618e26ab1)

## Sección 2) Desarrollo de la Aplicación Web
### Luego haz un pip install Flask
### Aparte crea la RDS desde la interfaz de AWS
### En el archivo app.py puedes ver el host, user, la base de datos y la password, todo esto tienes que cambiarlo segun lo crees en la rds
### para lo de mysql, usa estos comandos 
### sudo wget https://dev.mysql.com/get/mysql80-community-release-el9-1.noarch.rpm
### sudo dnf install mysql80-community-release-el9-1.noarch.rpm -y
### sudo rpm --import https://repo.mysql.com/RPM-GPG-KEY-mysql-2023
### sudo dnf install mysql-community-client -y
### sudo dnf install mysql-community-server –y

### sudo systemctl start mysqld
### sudo systemctl enable mysqld
### sudo systemctl status mysqld

### o	mysql -u admin -p -h el punto de enlace
### luego crea la base de datos CREATE TABLE IF NOT EXISTS datos(      id INT AUTO_INCREMENT PRIMARY KEY,      nombre VARCHAR(255),      edad INT,      genero VARCHAR(255)  );

![image](https://github.com/PedroAarom/Examen-practico-2/assets/166650957/fce93a2c-5f51-4751-8476-ae331d5eeeb3)

### aparte sudo yum install pymsql
