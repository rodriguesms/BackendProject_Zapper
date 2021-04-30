# Zapper Real Estate Agency

This is a personal backend project of a real estate agency backend application implementation.
The main objective is to apply these frameworks in a reality-close application and implement CRUD operations to a property management system.

_The following framework descriptions were collected from the framework's own personal site._

## Introduction

Originally, Zapper project was conceived using C/C++ in my Computer Enginnering graduation, for a programming course. 
The first project was developed using text files as an improvised database, and was able to register houses, apartments and lands for sale or rent. The user was be able to consult any registered property, filtering results by property type, price, or even the address.
This backend application was inspired by original Zapper, and represents not only a Zapper project update, but an update to myself as a developer.

#### Main programming language:

* Python

#### Frameworks used:

* [FastAPI](##FastAPI)
* [Uvicorn](##Uvicorn)
* [SQLAlchemy](##SQLAlchemy)
* [Psycopg2](##Psycopg2)
* [Alembic](##Alembic)
* [Passlib](##Passlib)

#### Database:

* [PostgreSQL](##PostgreSQL)

## FastAPI

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

The key features are:

* **Fast:** Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.
* **Fast to code:** Increase the speed to develop features by about 200% to 300%. *
* **Fewer bugs:** Reduce about 40% of human (developer) induced errors. *
* **Intuitive:** Great editor support. Completion everywhere. Less time debugging.
* **Easy:** Designed to be easy to use and learn. Less time reading docs.
* **Short:** Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
* **Robust:** Get production-ready code. With automatic interactive documentation.
* **Standards-based:** Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

_Source_: https://fastapi.tiangolo.com/


## Uvicorn

Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools.

Until recently Python has lacked a minimal low-level server/application interface for asyncio frameworks. The ASGI specification fills this gap, and means we're now able to start building a common set of tooling usable across all asyncio frameworks.

ASGI should help enable an ecosystem of Python web frameworks that are highly competitive against Node and Go in terms of achieving high throughput in IO-bound contexts. It also provides support for HTTP/2 and WebSockets, which cannot be handled by WSGI.

Uvicorn currently supports HTTP/1.1 and WebSockets. Support for HTTP/2 is planned.

_Source_: https://www.uvicorn.org/

## SQLAlchemy

SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.

SQL databases behave less like object collections the more size and performance start to matter; object collections behave less like tables and rows the more abstraction starts to matter. SQLAlchemy aims to accommodate both of these principles.

SQLAlchemy considers the database to be a relational algebra engine, not just a collection of tables. Rows can be selected from not only tables but also joins and other select statements; any of these units can be composed into a larger structure. SQLAlchemy's expression language builds on this concept from its core.

SQLAlchemy is most famous for its object-relational mapper (ORM), an optional component that provides the data mapper pattern, where classes can be mapped to the database in open ended, multiple ways - allowing the object model and database schema to develop in a cleanly decoupled way from the beginning.

SQLAlchemy's overall approach to these problems is entirely different from that of most other SQL / ORM tools, rooted in a so-called complimentarity- oriented approach; instead of hiding away SQL and object relational details behind a wall of automation, all processes are fully exposed within a series of composable, transparent tools. The library takes on the job of automating redundant tasks while the developer remains in control of how the database is organized and how SQL is constructed.

The main goal of SQLAlchemy is to change the way you think about databases and SQL!

_Source_: https://www.sqlalchemy.org/

## PostgreSQL

PostgreSQL is a powerful, open source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads. The origins of PostgreSQL date back to 1986 as part of the POSTGRES project at the University of California at Berkeley and has more than 30 years of active development on the core platform.

PostgreSQL has earned a strong reputation for its proven architecture, reliability, data integrity, robust feature set, extensibility, and the dedication of the open source community behind the software to consistently deliver performant and innovative solutions. PostgreSQL runs on all major operating systems, has been ACID-compliant since 2001, and has powerful add-ons such as the popular PostGIS geospatial database extender. It is no surprise that PostgreSQL has become the open source relational database of choice for many people and organisations.

_Source_: https://www.postgresql.org/

## Psycopg

Psycopg is the most popular PostgreSQL database adapter for the Python programming language. Its main features are the complete implementation of the Python DB API 2.0 specification and the thread safety (several threads can share the same connection). It was designed for heavily multi-threaded applications that create and destroy lots of cursors and make a large number of concurrent “INSERT”s or “UPDATE”s.

Psycopg 2 is mostly implemented in C as a libpq wrapper, resulting in being both efficient and secure. It features client-side and server-side cursors, asynchronous communication and notifications, “COPY TO/COPY FROM” support. Many Python types are supported out-of-the-box and adapted to matching PostgreSQL data types; adaptation can be extended and customized thanks to a flexible objects adaptation system.

Psycopg 2 is both Unicode and Python 3 friendly.

_Source_: https://pypi.org/project/psycopg2-binary/

## Alembic

Alembic provides for the creation, management, and invocation of change management scripts for a relational database, using SQLAlchemy as the underlying engine. This tutorial will provide a full introduction to the theory and usage of this tool.

Alembic is a database migrations tool written by the author of SQLAlchemy. A migrations tool offers the following functionality:

* Can emit ALTER statements to a database in order to change the structure of tables and other constructs
* Provides a system whereby “migration scripts” may be constructed; each script indicates a particular series of steps that can “upgrade” a target database to a new version, and optionally a series of steps that can “downgrade” similarly, doing the same steps in reverse.
* Allows the scripts to execute in some sequential manner.

_Source¹_: https://alembic.sqlalchemy.org/

_Source²_: https://pypi.org/project/alembic/

## Passlib

Passlib is a password hashing library for Python 2 & 3, which provides cross-platform implementations of over 30 password hashing algorithms, as well as a framework for managing existing password hashes. It’s designed to be useful for a wide range of tasks, from verifying a hash found in /etc/shadow, to providing full-strength password hashing for multi-user application.

_Source_: https://passlib.readthedocs.io/

### Data Schemas

<table>
    <tr>
        <th colspan="2">Houses</th>
        <th colspan="2">Apartments</th>
        <th colspan="2">Lands</th>
    </tr>
    <tr>
        <th>Type</th>
        <th>Data</th>
        <th>Type</th>
        <th>Data</th>
        <th>Type</th>
        <th>Data</th>
    </tr>
    <tr>
        <th><i>String</i></th>
        <th>Title</th>
        <th><i>String</i></th>
        <th>Title</th>
        <th><i>String</i></th>
        <th>Title</th>
    </tr>
    <tr>
        <th><i>String</i></th>
        <th>Zip Code</th>
        <th><i>String</i></th>
        <th>Zip Code</th>
        <th><i>String</i></th>
        <th>Zip Code</th>
    </tr>
    <tr>
        <th><i>String</i></th>
        <th>City</th>
        <th><i>String</i></th>
        <th>City</th>
        <th><i>String</i></th>
        <th>City</th>
    </tr>
    <tr>
        <th><i>String</i></th>
        <th>Neighborhood</th>
        <th><i>String</i></th>
        <th>Neighborhood</th>
        <th><i>String</i></th>
        <th>Neighborhood</th>
    </tr>
    <tr>
        <th><i>String</i></th>
        <th>Street</th>
        <th><i>String</i></th>
        <th>Street</th>
        <th><i>String</i></th>
        <th>Street</th>
    </tr>
    <tr>
        <th><i>Integer</i></th>
        <th>Address Number</th>
        <th><i>Integer</i></th>
        <th>Address Number</th>
        <th><i>Integer</i></th>
        <th>Address Number</th>
    </tr>
    <tr>
        <th><i>Bool</i></th>
        <th>Advertisement Definition</th>
        <th><i>Bool</i></th>
        <th>Advertisement Definition</th>
        <th><i>Bool</i></th>
        <th>Advertisement Definition</th>
    </tr>
    <tr>
        <th><i>Float</i></th>
        <th>Total Area</th>
        <th><i>Float</i></th>
        <th>Area</th>
        <th><i>Float</i></th>
        <th>Area</th>
    </tr>
    <tr>
        <th><i>Float</i></th>
        <th>Constructed Area</th>
        <th><i>Float</i></th>
        <th>-</th>
        <th><i>Float</i></th>
        <th>-</th>
    </tr>
    <tr>
        <th><i>Float</i></th>
        <th>-</th>
        <th><i>Float</i></th>
        <th>Condominium Price</th>
        <th><i>Float</i></th>
        <th>-</th>
    </tr>
    <tr>
        <th><i>Integer</i></th>
        <th>Number of Rooms</th>
        <th><i>Integer</i></th>
        <th>Number of Rooms</th>
        <th><i>Integer</i></th>
        <th>-</th>
    </tr>
    <tr>
        <th><i>Integer</i></th>
        <th>Number of Floors</th>
        <th><i>Integer</i></th>
        <th>-</th>
        <th><i>Integer</i></th>
        <th>-</th>
    </tr>
    <tr>
        <th><i>Integer</i></th>
        <th>-</th>
        <th><i>Integer</i></th>
        <th>Floor</th>
        <th><i>Integer</i></th>
        <th>-</th>
    </tr>
    <tr>
        <th><i>Integer</i></th>
        <th>-</th>
        <th><i>Integer</i></th>
        <th>Parking Spaces</th>
        <th><i>Integer</i></th>
        <th>-</th>
    </tr>
    <tr>
        <th><i>String</i></th>
        <th>-</th>  
        <th><i>String</i></th>
        <th>Sun Position</th>
        <th><i>String</i></th>
        <th>-</th>      
    </tr>
    <tr>
        <th><i>Float</i></th>
        <th>Price</th>
        <th><i>Float</i></th>
        <th>Price</th>  
        <th><i>Float</i></th>
        <th>Price</th>        
    </tr>   
</table>
