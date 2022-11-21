DROP TABLE IF EXISTS DiseaseType CASCADE;
DROP TABLE IF EXISTS Country CASCADE;
DROP TABLE IF EXISTS Disease CASCADE;
DROP TABLE IF EXISTS Discover CASCADE;
DROP TABLE IF EXISTS Users CASCADE;
DROP TABLE IF EXISTS PublicServant CASCADE;
DROP TABLE IF EXISTS Doctor CASCADE;
DROP TABLE IF EXISTS Specialize CASCADE;
DROP TABLE IF EXISTS Record CASCADE;

CREATE TABLE DiseaseType (
    id INT PRIMARY KEY,
    description VARCHAR(140) NOT NULL
);

CREATE TABLE Country (
    cname VARCHAR(50) PRIMARY KEY,
    population BIGINT NOT NULL
);

CREATE TABLE Disease (
    disease_code VARCHAR(50) PRIMARY KEY,
    pathogen VARCHAR(20) NOT NULL,
    description VARCHAR(140) NOT NULL,
    id INT NOT NULL,
    FOREIGN KEY (id) REFERENCES DiseaseType(id) ON DELETE CASCADE
);

CREATE TABLE Discover (
    cname VARCHAR(50),
    disease_code VARCHAR(50),
    first_enc_date DATE NOT NULL,
    PRIMARY KEY (cname, disease_code),
    FOREIGN KEY (cname) REFERENCES Country(cname),
    FOREIGN KEY (disease_code) REFERENCES Disease(disease_code) ON DELETE CASCADE   
);

CREATE TABLE Users (
    email VARCHAR(60) NOT NULL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    surname VARCHAR(40) NOT NULL,
    salary INT NOT NULL,
    phone VARCHAR(20) NOT NULL,
    cname VARCHAR(50) NOT NULL,
    FOREIGN KEY (cname) REFERENCES Country(cname)
);

CREATE TABLE PublicServant (
    email VARCHAR(60) NOT NULL PRIMARY KEY,
    department VARCHAR(20) NOT NULL,
    FOREIGN KEY (email) REFERENCES Users(email) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Doctor (
    email VARCHAR(60) NOT NULL PRIMARY KEY,
    degree VARCHAR(20) NOT NULL,
    FOREIGN KEY (email) REFERENCES Users(email) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Specialize (
    id INT,
    email VARCHAR(60),
    PRIMARY KEY (id, email),
    FOREIGN KEY (id) REFERENCES DiseaseType(id),
    FOREIGN KEY (email) REFERENCES Doctor(email) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Record (
    email VARCHAR(60),
    cname VARCHAR(50),
    disease_code VARCHAR(50),
    total_deaths INT NOT NULL,
    total_patients INT NOT NULL,
    PRIMARY KEY (email, cname, disease_code),
    FOREIGN KEY (disease_code) REFERENCES Disease(disease_code),
    FOREIGN KEY (cname) REFERENCES Country(cname),
    FOREIGN KEY (email) REFERENCES PublicServant(email) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO diseasetype(id, description) VALUES (1, 'lungs disease'), 
                                                (2, 'head disease'), 
                                                (3, 'intestine disease'), 
                                                (4, 'infectious disease'), 
                                                (5, 'virology'),
                                                (6, 'stomach disease'),
                                                (7, 'deficiency'),
                                                (8, 'allergy'),
                                                (9, 'mental disease'),
                                                (10, 'cancer');

INSERT INTO disease(disease_code, pathogen, description, id) VALUES ('Z11.1', 'bacteria', 'Tuberculosis', 1),
                                                                    ('G03.9', 'bacteria', 'Meningitis', 2), 
                                                                    ('ICD-10', 'bacteria', 'Cholera', 3),
                                                                    ('B20', 'virus', 'HIV/AIDS', 4),
                                                                    ('covid-19', 'virus',     'Severe disease',   5),
                                                                    ('ADHD', 'no pathogen', 'Attention deficit hyperactivity', 9),
                                                                    ('TN-56', 'anaphylaxis', 'Tree nut allergy', 8),
                                                                    ('DH9.0', 'bacteria', 'Diarrhea', 6),
                                                                    ('IR-8.6', 'no pathogen', 'Iron deficiency', 7),
                                                                    ('LC.34', 'no pathogen', 'Lung cancer', 10);

INSERT INTO country(cname, population) VALUES ('China', 1500000000), 
                                              ('USA', 345000000), 
                                              ('Italy', 87000000), 
                                              ('Russia',145934462),
                                              ('Switzerland', 87654324),
                                              ('Ireland', 3400567),
                                              ('France', 23400056),
                                              ('UK', 67330000),
                                              ('Iceland', 42700000),
                                              ('Japan', 629000000);

INSERT INTO discover(cname, disease_code, first_enc_date) VALUES ('USA', 'Z11.1', '1882-05-24'),
                                                                ('USA', 'G03.9', '1661-04-28'),
                                                                ('Italy', 'ICD-10', '1994-09-11'),
                                                                ('USA', 'B20', '1990-08-05'),
                                                                ('China','covid-19', '2019-11-18'),
                                                                ('Russia','covid-19', '2007-11-21'),
                                                                ('UK', 'covid-19', '2022-01-01'),
                                                                ('France', 'covid-19', '2021-08-09'),
                                                                ('Iceland', 'DH9.0', '1998-01-03'),
                                                                ('Ireland', 'covid-19', '2019-09-09');

INSERT INTO users(email, name, surname, salary, phone, cname) VALUES ('zhumagl@gmail.com', 'Lyazzat', 'Zhumagulova', 350000, '+77089204408', 'USA'),
                                                                    ('akadyrov@gmail.com', 'Askarbek', 'Kadyrov', 800000, '+77017201175', 'USA'),
                                                                    ('marssan@gmail.com', 'Sanzhar', 'Mars', 950000, '+77089204407', 'Italy'),
                                                                    ('marsanuar@gmail.com', 'Anuar', 'Mars', 1050000, '+77085462233', 'China'),
                                                                    ('isataiaiman@gmail.com', 'Aiman', 'Isatai', 1250000, '+77085439233', 'China'),
                                                                    ('yernarmars@gmail.com', 'Yernar', 'Mars', 980000, '+77115439233', 'Russia'),
                                                                    ('inkarmars@gmail.com', 'Inkar', 'Mars', 1030000, '+77115498233', 'Russia'),
                                                                    ('navalravikant@gmail.com', 'Naval', 'Ravikant', 2300000, '+447084014247', 'UK'),
                                                                    ('harrypotter@gmail.com', 'Harry', 'Potter', 987000, '+457084913267', 'Ireland'),
                                                                    ('kjtokayev@gmail.com', 'KJ', 'Tokayev', 999999999, '+77777777777', 'France'),

                                                                    ('xijinping@gmail.com', 'Xi', 'Jinping', 42500, '+89000824', 'China'),  
                                                                    ('pijinping@gmail.com', 'Pi', 'Jinping', 43500, '+87000824', 'France'),  
                                                                    ('mijinping@gmail.com', 'Mi', 'Jinping', 44500, '+89000924', 'Ireland'), 
                                                                    ('yijinping@gmail.com', 'Yi', 'Jinping', 48500, '+89080824', 'China'),   
                                                                    ('lijinping@gmail.com', 'Li', 'Jinping', 52500, '+89010824', 'Japan'),  
                                                                    ('kijinping@gmail.com', 'Ki', 'Jinping', 46500, '+89900824', 'USA'),  
                                                                    ('wijinping@gmail.com', 'Wi', 'Jinping', 82500, '+89000924', 'Russia'),                                                        
                                                                    ('kausarmars@gmail.com', 'Kausar', 'Mars', 450000, '+77084014247', 'Russia'),
                                                                    ('zangarmars@gmail.com', 'Zangar', 'Mars', 650000, '+77084024247', 'China'),
                                                                    ('zhemismars@gmail.com', 'Zhemisgul', 'Mars', 500000, '+77094014247', 'China');

INSERT INTO doctor(email, degree) VALUES ('zhumagl@gmail.com', 'MD'),
                                        ('akadyrov@gmail.com', 'MS'),
                                        ('marssan@gmail.com', 'MD'),
                                        ('marsanuar@gmail.com', 'PhD'),
                                        ('isataiaiman@gmail.com','PhD'),
                                        ('yernarmars@gmail.com', 'MS'),
                                        ('inkarmars@gmail.com', 'MD'),
                                        ('navalravikant@gmail.com', 'MD'),
                                        ('harrypotter@gmail.com', 'PhD'),
                                        ('kjtokayev@gmail.com', 'MD');


INSERT INTO specialize(id, email) VALUES (4, 'zhumagl@gmail.com'),
                                        (2, 'akadyrov@gmail.com'),
                                        (1, 'marssan@gmail.com'),
                                        (1, 'marsanuar@gmail.com'),
                                        (2, 'marsanuar@gmail.com'),
                                        (5, 'marsanuar@gmail.com'),
                                        (5, 'isataiaiman@gmail.com'),
                                        (1, 'yernarmars@gmail.com'),
                                        (5, 'yernarmars@gmail.com'),
                                        (3, 'inkarmars@gmail.com'), 
                                        (5, 'inkarmars@gmail.com');


INSERT INTO publicservant(email, department) VALUES ('kausarmars@gmail.com',  'Dept1'),
                                                    ('zangarmars@gmail.com',  'Dept2'),
                                                    ('zhemismars@gmail.com',  'Dept1'),
                                                    ('xijinping@gmail.com', 'Dept3'),
                                                    ('pijinping@gmail.com', 'Dept4'),
                                                    ('mijinping@gmail.com', 'Dept4'),
                                                    ('yijinping@gmail.com', 'Dept5'),
                                                    ('lijinping@gmail.com', 'Dept5'),
                                                    ('kijinping@gmail.com', 'Dept6'),
                                                    ('wijinping@gmail.com', 'Dept6');


INSERT INTO record(email, cname, disease_code, total_deaths, total_patients) VALUES ('kausarmars@gmail.com', 'Russia', 'covid-19', 555444, 666777),
                                                                                    ('zangarmars@gmail.com', 'China', 'covid-19', 2223333, 4445555),
                                                                                    ('zhemismars@gmail.com', 'China', 'covid-19', 12356, 56789),
                                                                                    ('kausarmars@gmail.com', 'USA', 'covid-19', 10, 15),
                                                                                    ('zangarmars@gmail.com', 'USA', 'covid-19', 20, 25),
                                                                                    ('kausarmars@gmail.com', 'China', 'covid-19', 30, 35),
                                                                                    ('zangarmars@gmail.com', 'Russia', 'covid-19', 40, 45),
                                                                                    ('zangarmars@gmail.com', 'Italy', 'covid-19', 45, 50),
                                                                                    ('zhemismars@gmail.com', 'China', 'B20', 1256, 5678),
                                                                                    ('xijinping@gmail.com', 'France', 'covid-19', 888888, 999777);