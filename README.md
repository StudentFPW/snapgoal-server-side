## Database

| Database | Description |
|----------|-------------|
| Product  | Product catalog with details like price, category, and availability |

---

## Database data-Type

| Database | Data-type (object_type) | Description |
|----------|-------------------------|-------------|
| Product  | product                 | tag         |

---

## Object: product

Products in the store, including their details and availability.

| Naming           | Description                                               | Type                  | Unique | Required |
|------------------|-----------------------------------------------------------|-----------------------|--------|----------|
| object_type      | Type of object                                            | String 'product'       | No     | Yes      |
| Attr **data**:   |                                                           |                       |        |          |
| title            | Name of the product                                        | String                | No     | Yes      |
| description      | Detailed description of the product                        | String                | No     | No       |
| uuid| Unique object identifier                                            | UUID       | Yes     | Yes      |
| price            | Price of the product                                       | Integer  | No     | Yes      |
| image            | URL of the product image                                   | String (e.g., "image1.jpg") | No     | Yes      |
| category         | Category of the product (e.g., electronics, clothing)      | String                | No     | Yes      |
| availability     | Availability status (in stock, out of stock)              | Bool | No     | Yes      |
| feedback         | Feedback or review score from customers                    | Decimal (1-5)          | No     | No       |


## Object: cart

| Naming           | Description                                               | Type                  | Unique | Required |
|------------------|-----------------------------------------------------------|-----------------------|--------|----------|
| items         | Products in the cart    | Product array | No     | Yes       |

