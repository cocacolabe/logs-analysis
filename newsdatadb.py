# Python Version: 2.7.13
#! /usr/bin/env python
import psycopg2


def first_report():
    # connect to the database
    db = psycopg2.connect("dbname=news")
    # make an object "cursor", which runs query and fetch results
    c = db.cursor()
    # execute a query using a cursor
    result = c.execute(" select title, \
        count(path) as view \
        from articles \
        join log \
        on articles.slug = substr(log.path,10) \
        group by title\
        order by view desc\
        limit 3;")
    # using cursor to fetch data
    report = c.fetchall()
    print "\n\n", "1. The most popular three articles of all time:\n"
    for row in report:
        title = row[0]
        count = row[1]
        print "**", title, "-", count, "views\n"
    # close connection when you are done
    db.close()


first_report()


def second_report():

    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    result = c.execute(" select name, count(path) as view \
        from articles ar \
        inner join authors au \
        on ar.author = au.id \
        inner join log \
        on ar.slug = substr(log.path, 10)\
        group by name\
        order by view desc;")
    report = c.fetchall()
    print "\n\n", "2. The most popular article authors of all time:\n"
    for row in report:
        author = row[0]
        count = row[1]
        print "**", author, "-", count, "views\n"
    db.close()


second_report()


def last_report():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    result = c.execute(" select date, result \
        from errorpercent \
        where result > 0.01;")
    report = c.fetchall()
    percent = '%'
    print "\n\n", "3. Days that more than 1", percent,\
        "of requests lead to errors:\n"
    for row in report:
        day = row[0]
        error = row[1]
        print "**", day, "-", error * 100, percent, "errors"
    db.close()


last_report()
