# Day 33 - APIs

On day 33, the concept of API was introduced, this is a small script that makes calls to the ISS Overhead API.

The ISS is a satelite that is on constant movement around the world. 

Through this script, an e-mail is sent to the receiver specified on the .env file when the ISS is close to the specified geographic location.

In addition, a second API is used to define is it is dark time or not, making it so that, the e-mail is only sent during night times.
