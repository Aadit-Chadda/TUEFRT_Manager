"""

TABLES SUGGESTIONS:

----
Inventory:
- product id (primary key)
- product name
- quantity
----

----
Oxygen Tanks:
- product id (foreign key)
- tank id (primary key)
- pack number (backpack)
- psi (how much air)
    
    Questions:
    - how do you identify which tank goes into which backpack?
    - how do you identify tanks? Is there like an id/name?
----

----
Epipen:
- product id (foreign key)
- epipen id (primary key)
- expiry date
----

----
Inventory Used:
- record id (primary key)
- product id (foreign key)
- quantity
- date
- expired or damaged/used/lost?
----

----
Orders Made:
- order id (composite primary key)
- date ordered
- supplier
- product id (foreign key) (composite primary key)
- quantity
- date received --> when first ordered - "waiting for shipment", when received - input date
----


    Questions for TUFERT:
    - do you have a master list of inventory?
    - how do you keep track of inventory? (any forms)
    - what items do you keep track of?
    - do you keep track of your suppliers?
    - besides the quantity, is there any other characteristic you keep track of? (e.g. oxygen tank psi, expiry date)
    - is there anything else we are missing/ anything else we should add?

    Future Concerns:
    - where do we put inventory used/shipments data once it's old? --> DWH? Does Trent have a DWH we could connect our app to?

"""