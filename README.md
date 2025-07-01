<svg fill="none" viewBox="0 0 600 300" width="600" height="300" xmlns="http://www.w3.org/2000/svg">
  <foreignObject x="0" y="0" width="600" height="300"> 
  <div xmlns="http://www.w3.org/1999/xhtml">
      <h1  align="center" >Budget Tracker</h1>
      <p align="center">Manage your finances effectively.</p>
    </div>

---
<div>
  <h3>Table Of Contents</h3>
  <ol>
    <li>About</li>
    <li>Problem Statement</li>
    <li>Architecture Overview
      <ul>
        <li>Design Pattern</li>
        <li>Backend architecture</li>
      </ul>
    </li>
    <li>Project source code</li>
    <li>Tech Stack</li>
    <li>Guidelines</li>
    <li>Conclusion</li>
  </ol>
</div>

  ---
<div>
    <h3 font="bold">1. About </h3>
    <br>
    <p>
      This project is to build a user-friendly application that helps individuals track their savings and expenses on a daily, monthly, and yearly basis, providing real-time reports and notifications.
    </p>
</div>

---

<div>
  <h3>2. Problem Statement</h3>
  <p>
    People often invest in stocks or spend money for their needs without a clear picture of their actual financial position. Relying on manual calculations or checking bank statements is inefficient. This project provides a platform that enables users to automatically track and visualize their financial data effectively.
  </p>
</div>
<div>
</div>

---

<div>
  <div>
    <h3>3. Architecture Overview</h3>
  </div>
  <div>
    <h4>🏗️ Design Pattern : MVC Architecture (Model View Controller)</h4>
     <ul>
      <li>View : User interacts with applications & represents data visually</li>
      <li>Controller : Request from view will be redirected to business logic, manages the resources and provides response to view</li>
      <li>Model : Business Logic stands for performing all the operations on expense, savings & performing CRUD operations on it. Generating report</li>
    </ul>
    <div>
       <h4>🧩 Backend Architecture : Microservices</h4>
    </div>
  </div>

   | Title | Description |
   | ----  | ------------|    
   | Auth Services | Manages registeration, signin using OAuth google & aplication login / registeration services |
   | Budget Services | CRUD operations on expense, create/ update savings, create/update salary |
   | Mail Services | Sends the update via mails |
   | Report Services | Generates the report on monthly weekly, yearly basis |

  ---
  <div>
    <h3>4. Project source code link 👇 </h3>
  </div>

  |Title | Code Link |
  | ---- | --------- |
  |View  | <a href="https://github.com/Shwetha-75/Budget-Tracker-View.git" target="_blank">View</a>
  |Auth Services | <a href="https://github.com/Shwetha-75/registration-services-budget-tracker.git" target="_blank">Register</a> |
  |     | <a href="https://github.com/Shwetha-75/budget-tracker-login-services.git" target="_blank">Login</a>|
  |     | <a href="https://github.com/Shwetha-75/Google-SignIn.git" target="_blank">OAuth Google SignIn</a> |
  |Budget Services | <a href="https://github.com/Shwetha-75/budget-tracker-budget-services.git" target="_blank">Budget Services</a> |

  ---

  <div>
    
  </div>
  <h3>5. Tech Stack</h3>
  
  |Phase | Tech |
  |------- |------|
  |Frontend| Reactjs |
  |Backend | Flask using python, OAuth SignIn |
  |Databse |Firebase |
  |Testing | .rest, pytest, postman |
  |Deloyement | render, vercel|

  ---

  <div>
    <h3>6. Guidelines to deploy on local </h3>
  </div>
   <p>Clone the repositories</p>
   
   ~~~
    git clone https://github.com/Shwetha-75/Budget-Tracker-View.git
   ~~~
   ~~~
    git clone https://github.com/Shwetha-75/registration-services-budget-tracker.git
   ~~~
   ~~~
    git clone https://github.com/Shwetha-75/budget-tracker-login-services.git
   ~~~
   ~~~
    git clone https://github.com/Shwetha-75/Google-SignIn.git
   ~~~
   ~~~
    git clone https://github.com/Shwetha-75/budget-tracker-budget-services.git
   ~~~

   <p>For view install lastest version & integrate it with vite (Optional : you can use any flavours of js and frameworks)</p>

   ~~~
     npm create vite@latest
   ~~~
   <p>Install node modules</p>

   ~~~
    npm i
   ~~~
   <p>For Backend services install the requirements.txt file, firstly set up the virtual env & activate it</p>

   ~~~
     pip install -r file_path(requirements.txt )
   ~~~

  ---
  
  <h3>Conclusion</h3>
  <div>
    <ul>
      <li>Contributors : Shwetha K (Design, Develeopment, Deployment)</li>
      <li>**Note : No fixed timeline, the project is under development.</li>
    </ul>
  </div>
  <p>"Woohoo!" 🎉 you have completed the installation, now you can work on the project to implement your own ideas</p>
 </div>
  </foreignObject>
</svg>
