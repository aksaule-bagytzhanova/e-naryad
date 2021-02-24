# E-naryad
## Personal website 
Description: Web page for interaction between employees in big company. The key task of the site:
- Order processing requests
- Acceptance or rejection of a document
- Ability to write emails between employees
- Ability to write progress report

**Team members:**

- Bagytzhanova Aksaule
- Baturhanova Aida
- Kurmangalieva Madina

## Website Pages
1. **Login page**

Employee authorization

2. **E-naryad**

This is the main page that shows all the latest news, which outfits have been submitted for confirmation with dates, the number of completed outfits and the number of completed work.

3. **Order**

Drawing up and registering the work done for confirmation 

4. **Service passport**

Drawing up and creating a service passport. In total, 6 passports and an archive of passports.

5. **Efficiency calculation**

The page where it shows what costs were and statistics on it.

6. **Admin panel**

Member admin page, personal data, employee photo.

7. **Posts**

## Q/A

### 1

In general, what does the site do?

The site has been reassigned so that employees can safely and quickly agree on the start of new projects and so that it can be seen how many hours an employee works per day.

### 2

What are the main members of the group?

Site members are the first group of ordinary workers, managers and director.

### 3

Who will fill in all the data?

All data is created by ordinary workers. They create data to get started.

### 4

Who will allow, give consent to the work done?

The first group of people who give consent are managers, and finally give consent to start doing it the director.

### 5

What data will be in the admin panel?

Name, position, last visit to the site, total arrival on the site.

### 6

What does the “Calculation of efficiency” section answer?

Efficiency calculation is a page where you can see how much material was spent and how much was spent on this work.

### 7

To enter the system, an employee must register or will he be given a username and password?

Each person who holds a position in this company will be registered in the database and each person will be given their own username and password.

### 8

And if, when creating a new electronic order, managers do not give permission to work, what will happen?

If the managers and the director turn out, then he will have to write the reason for the refusal and give recommendations for filling.

### 9 

Will you have to enter new data every day or is it unnecessary?

It is not necessary to update the site every day, but on the main page where you need to show the news of the week, you will need to update the news part every week.

### 10

What architectural model did you choose?

For the implementation of our project, MVC architectural design is most suitable. We want to use this method because of dividing the application data, user interface and control logic into three separate components: model, view, and controller, so we can develop each part independently. This model will be useful for displaying data in the form of a spreadsheet, bar graph, and pie chart due to the fact that you can reuse the code. Also, this model is convenient for dividing work into a group. Another model that is necessary is Client-Server Architecture. It has its advantages such as Recovery does not require high maintenance costs and the ability to recover data. The capacity of the Client can be changed separately, and Servers can be changed separately. But it still has its disadvantages: Clients are susceptible to viruses, trojans if they are present on the server or downloaded to the Server. The server is susceptible to denial of service (DDOS) attacks. Data packets can be tampered with or altered during transmission. Phishing or collecting credentials or other useful information about a user is common, and MITM (Man in the Middle) attacks are common. Overall, we think that advantages overweigh disadvantages and the architecture fits our project. We will also use Layered Architecture. There are tons of necessary features of the Layered model. For example, if a person can see his history through the site, how he entered or how many hours he worked, he can see several platforms because of this, this model is convenient, is functional, and layers allow you to better customize the system As we know, layered architecture consists of five parts, and I want to discuss each part of how it is useful for us: User interaction level: This is a report, a form, a menu and it shows us how our application looks like. Functionality level: This function determines how the functions work and how the methods work, for example, how the buttons work because of this we use this Layer and this also proves to us that we should work with the layer model Business rules layer: This explains to us what our project can do, for example, analyze how many people have come to work today, how many people have forgotten their cards, this all helps the economist in calculating money Application core layer: It all depends on the programming language, all programmers work here most of all, this layer determines, or we can say it waits for the result from the code Database level: Here we work purely with tables, SQL queries and this layer basically adds combines the tables make it unique, it also changes the main things and we need all this, I would write SQL queries here, but the project is not ready yet because of this it's enough for now And this Layer is different to us for this reason. Yes, there are some nuances, but I think we will still avoid these nuances about it.

### 11

What technologies do you use?

For the backend we use Django, for the frontend html, css and js, for the database we use SQLite

### 12

What kind of tables are there?

That is, we have a general information table, this is name, time of stay, position, and so on. Then we have a table of the work done, at the present moment what work is being done. And a table for adding efficiency calculation.

### 13

You have a table for time?

That is, we have a time table, it will be updated every time an employee sits on the site.



