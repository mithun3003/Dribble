# Project Responsive Web Design using Bootstrap
## Date: 15/11/2025

## AIM:
To create a simplified clone of Dribbble (https://dribbble.com/) landing page.


## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Insert the necessary CSS and JavaScript files as external in order to use Bootstrap.

### Step 5:
Create a HTML file and include the needed Bootstrap components.

### Step 6:
Publish the website in the LocalHost.

## PROGRAM :

```
## INDEX.HTML

{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Mini Dribbble Clone</title>

  <!-- Bootstrap CSS CDN -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<body class="bg-light">

  <!-- NAVBAR -->
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid px-4">

      <a class="navbar-brand fw-bold" href="{% url 'home' %}">
        dribbble<span class="text-danger">•mini</span>
      </a>

      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mainNav">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="mainNav">

        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item"><a class="nav-link active" href="{% url 'home' %}">Shots</a></li>
          <li class="nav-item"><a class="nav-link" href="{% url 'designers' %}">Designers</a></li>
          <li class="nav-item"><a class="nav-link" href="{% url 'teams' %}">Teams</a></li>
          <li class="nav-item"><a class="nav-link" href="{% url 'community' %}">Community</a></li>
          <li class="nav-item"><a class="nav-link" href="{% url 'jobs' %}">Jobs</a></li>
        </ul>

        <!-- Search Form -->
        <form class="d-flex me-3" method="get" action="{% url 'search' %}">
          <input class="form-control form-control-sm me-2" type="search" name="q" placeholder="Search">
          <button class="btn btn-outline-light btn-sm" type="submit">Go</button>
        </form>

        <!-- Sign in / Sign up -->
        <div class="d-flex">
          <a href="{% url 'signin' %}" class="btn btn-outline-light btn-sm me-2">Sign in</a>
          <a href="{% url 'signup' %}" class="btn btn-danger btn-sm">Sign up</a>
        </div>

      </div>
    </div>
  </nav>

  <!-- HERO -->
  <section class="bg-white border-bottom text-center py-4">
    <h4 class="fw-semibold">What are you working on?</h4>
    <p class="text-muted mb-0">Dribbble is show and tell for designers. Explore the latest shots below.</p>
  </section>

  <!-- SHOTS GRID -->
  <main class="container py-5">
    <div class="row g-4">

      <!-- Card 1 -->
      <div class="col-6 col-md-4 col-lg-3">
        <div class="card h-100 shadow-sm">
          <img src="{% static 'dribbleapp/img/shot1.jpg' %}" class="card-img-top" alt="Shot 1">
          <div class="card-body py-2">
            <h6 class="card-title mb-1">Dark UI Concept</h6>
            <p class="card-text small text-muted mb-0">by Designer • 300 likes</p>
          </div>
        </div>
      </div>

      <!-- Card 2 -->
      <div class="col-6 col-md-4 col-lg-3">
        <div class="card h-100 shadow-sm">
          <img src="{% static 'dribbleapp/img/shot2.jpg' %}" class="card-img-top" alt="Shot 2">
          <div class="card-body py-2">
            <h6 class="card-title mb-1">Landing Page</h6>
            <p class="card-text small text-muted mb-0">by Designer • 250 likes</p>
          </div>
        </div>
      </div>

      <!-- Card 3 -->
      <div class="col-6 col-md-4 col-lg-3">
        <div class="card h-100 shadow-sm">
          <img src="{% static 'dribbleapp/img/shot3.jpg' %}" class="card-img-top" alt="Shot 3">
          <div class="card-body py-2">
            <h6 class="card-title mb-1">Dashboard</h6>
            <p class="card-text small text-muted mb-0">by Designer • 180 likes</p>
          </div>
        </div>
      </div>

      <!-- Card 4 -->
      <div class="col-6 col-md-4 col-lg-3">
        <div class="card h-100 shadow-sm">
          <img src="{% static 'dribbleapp/img/shot4.jpg' %}" class="card-img-top" alt="Shot 4">
          <div class="card-body py-2">
            <h6 class="card-title mb-1">Illustration</h6>
            <p class="card-text small text-muted mb-0">by Designer • 120 likes</p>
          </div>
        </div>
      </div>

    </div>
  </main>

  <!-- FOOTER -->
  <footer class="bg-dark text-white mt-4">
    <div class="container text-center py-3">
      <p class="mb-1 small">&copy; 2025 Mini Dribbble Clone</p>
      <p class="mb-0 small">Designed by <strong>MITHUN S</strong></p>
    </div>
  </footer>

  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>

```
```
## DESIGNERS.HTML

{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Designers</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
  <div class="container py-5">
    <h2>Designers</h2>
    <p>This is a placeholder page for Designers.</p>
    <a href="{% url 'home' %}" class="btn btn-secondary btn-sm">Back to Home</a>
  </div>
</body>
</html>

```
```
## TEAMS.HTML

{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Teams</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
  <div class="container py-5">
    <h2>Teams</h2>
    <p>This is a placeholder page for Teams.</p>
    <a href="{% url 'home' %}" class="btn btn-secondary btn-sm">Back to Home</a>
  </div>
</body>
</html>

```
```
## COMMUNITY.HTML

{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Community</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
  <div class="container py-5">
    <h2>Community</h2>
    <p>This is a placeholder page for Community.</p>
    <a href="{% url 'home' %}" class="btn btn-secondary btn-sm">Back to Home</a>
  </div>
</body>
</html>

```
```
## JOBS.HTML

{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Jobs</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
  <div class="container py-5">
    <h2>Jobs</h2>
    <p>This is a placeholder page for Jobs.</p>
    <a href="{% url 'home' %}" class="btn btn-secondary btn-sm">Back to Home</a>
  </div>
</body>
</html>

```
```
## SIGNIN.HTML

{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Sign In</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
  <div class="container py-5" style="max-width: 420px;">
    <h3 class="mb-4">Sign In</h3>

    <form>
      <div class="mb-3">
        <label>Email</label>
        <input type="email" class="form-control" placeholder="Enter email">
      </div>

      <div class="mb-3">
        <label>Password</label>
        <input type="password" class="form-control" placeholder="Enter password">
      </div>

      <button class="btn btn-dark w-100" type="submit">Sign In</button>
    </form>

    <a href="{% url 'home' %}" class="btn btn-secondary btn-sm mt-3">Back to Home</a>
  </div>
</body>
</html>

```
```
## SIGNUP.HTML

{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Sign Up</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
  <div class="container py-5" style="max-width: 420px;">
    <h3 class="mb-4">Create an Account</h3>

    <form>
      <div class="mb-3">
        <label>Name</label>
        <input type="text" class="form-control" placeholder="Enter name">
      </div>

      <div class="mb-3">
        <label>Email</label>
        <input type="email" class="form-control" placeholder="Enter email">
      </div>

      <div class="mb-3">
        <label>Password</label>
        <input type="password" class="form-control" placeholder="Enter password">
      </div>

      <button class="btn btn-danger w-100" type="submit">Sign Up</button>
    </form>

    <a href="{% url 'home' %}" class="btn btn-secondary btn-sm mt-3">Back to Home</a>
  </div>
</body>
</html>

```
```
## SEARCH.HTML

{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Search Results</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
  <div class="container py-5">
    <h2>Search Results</h2>

    <p>You searched for:  
      <strong>{{ query }}</strong>
    </p>

    <p>(Search is not implemented — this is only a UI page.)</p>

    <a href="{% url 'home' %}" class="btn btn-secondary btn-sm">Back to Home</a>
  </div>
</body>
</html>

```

## OUTPUT:

![alt text](<Screenshot 2025-11-15 185153.png>)

## RESULT:
The Project for responsive web design using Bootstrap is completed successfully.
