-- this script trigger decreases the quantity of an item,
-- after an item added to the order

DELIMITER $$

CREATE TRIGGER decrease_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE id = NEW.item_name;
END;
$$

DELIMITER ;
