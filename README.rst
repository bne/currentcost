===================================
Collect data from CurrentCost Meter
===================================

Introduction
============

The goals of this project are simple - provide a daemon
that collects data from a CurrentCost meter and stores it
in one of a variety of data stores.

TODO
====

 * Build SQLAlchemy models
 * Set up the datastore part of the configuration file
 * Write the daemon
 * Look into connecting to Pachube
 * Look into Mongo and Couch for the NOSQL nutters
 
Plan
====

Runner:
-------
 * Takes a config object
 * Controls frequency of run
 * Pass it a reader object (CurrentCost) and a writer object
 * It handles the rest

Reader:
-------
 * Talks to the meter
 * Provides a standard interface
 
Reference
=========

 * XML format: http://cumbers.wordpress.com/2008/05/07/breakdown-of-currentcost-xml-output/

Pre-requisites
==============

At this precise moment the following Ubuntu python packages are required:

 * python-serial
 * python-sqlalchemy
 