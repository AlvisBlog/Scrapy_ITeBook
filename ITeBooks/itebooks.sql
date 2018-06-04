-- auto-generated definition
USE itebooks;


-- auto-generated definition
CREATE TABLE book_info
(
  id               INT AUTO_INCREMENT
    PRIMARY KEY,
  book_id          INT          NOT NULL,
  book_isbn        VARCHAR(100) NULL,
  book_detail_link VARCHAR(200) NULL,
  book_author      VARCHAR(200) NULL,
  book_name        VARCHAR(100) NULL,
  book_page        INT          NULL,
  book_pub_year    VARCHAR(50)  NULL,
  book_language    VARCHAR(20)  NULL,
  book_size        VARCHAR(10)  NULL,
  book_format      VARCHAR(10)  NULL,
  book_category    VARCHAR(250) NULL,
  book_description LONGTEXT     NULL,
  book_down_link   VARCHAR(200) NULL,
  book_img_url     VARCHAR(250) NULL,
  CONSTRAINT book_info_id_uindex
  UNIQUE (id),
  CONSTRAINT book_info_book_id_uindex
  UNIQUE (book_id)
);

