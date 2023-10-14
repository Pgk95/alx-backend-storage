-- this script trigger decreases the quantity of an item,
-- after an item added to the order

DELIMITER $$

CREATE TRIGGER decrease_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - 1
    WHERE id = NEW.item_id;
END;
$$

DELIMITER ;
