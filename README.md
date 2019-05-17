# flask代码重构

## SQL重构思路

- 权限表（Role）

列名|数据类型|主键、索引、外键、唯一、/
-----|----|----
id|int|主键
name|string|/

- 用户表（User）

列名|数据类型|主键、索引、外键、唯一、/
-----|----|----
id|int|主键
name|string|索引
password_hash|string|/
factory_id|string|/

- 设备表（Equipment）

列名|数据类型|主键、索引、外键、唯一、/
-----|----|----
id|int|主键
eid|string|联合索引fid
fid|string|联合索引eid
place|string|唯一
supplier|string|/
spl_address|string|/
spl_contact|string|/
Timestamp|datetime|索引（有默认值）
SencerNum|int|/
SencerName|string|/
NoLoad_set|string|/
EmptyLoad_set|string|/
Temp|float|/
Wet|float|/
ExcV|float|/
Sensitivity|float|/
Resistance|int|/

- 趋势表（Thread）

列名|数据类型|主键、索引、外键、唯一、/
-----|----|----
id|int|主键
Timestamp|datetime|索引（有默认值）
standard|float|/
zeropoint|float|/

- 设备运行情况表（stateList）

列名|数据类型|主键、索引、外键、唯一、/
-----|----|----
id|int|主键
Timestamp|datetime|索引（有默认值）
RecoverTime|datetime|/
PeriodSecond|int|/
FaultSencer|string|索引
FaultCode|int|索引
FaultState|bool|/
record|string|/
eid|int|外键（Equipment）

- 每天自建新表（NewVal）

列名|数据类型|主键、索引、外键、唯一、/
-----|----|----
id|int|主键
Timestamp|datetime|索引（有默认值）
WeightTag1|float|/
WeightTag2|float|/
WeightTag3|float|/
WeightTag4|float|/
Weight|float|/

- 每天自建错误信息表（FaultMsg）（与原来相同，多一列外键）

- 测试用表（test_water）