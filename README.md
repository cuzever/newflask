# flask代码重构

## SQL重构思路

- 权限表（Role）

列名|数据类型|主键、索引、/|unique
-----|----|----|----
id|string|主键|是
name|string|/|否

- 用户表（User）

列名|数据类型|主键、索引、/|unique
-----|----|----|----
id|