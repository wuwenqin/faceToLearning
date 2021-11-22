# 												锁





### 1. 一致性非锁定读

指InnoDB存储引擎通过**多版本控制**的方式来读取当前执行时间数据库中行的数据。如果读取的行正在执行DELETE或UPDATE操作，此时的读取操作不会因此去等待行上的锁释放。相反地，InnoDB存储引擎会去**读取行的一个快照数据**。

一致性非锁定读之所以成为非锁定读，因为不需要等待访问数据行的X锁的释放。**快照数据是指该行数据的之前版本**，该实现**通过undo log完成**。而undo是用来**事务回滚的数据**，因此快照数据本身没有额外的开销；此外快照数据不需要上锁，因为**没有事务需要对历史数据进行修改操作**。



一致性非锁定读机制极大的提高了数据库的并发性。在InnoDB存储引擎的默认设置下，这个默认的读取方式，即读取不会占用和等待表上的锁（SELECT ... FOR UPDATE/SELECT ... LOCK IN SHARE MODE除外）；一致性行非锁定读，用到到数据的之前的历史版本，可能会有多个历史版本，由此带来的并发控制，就是大名鼎鼎的 **多版本并发控制（MVCC）**。



MYSQL数据库InnoDB存储引擎支持4中事务隔离级别，并不是每个事务隔离级别都采用一致性非锁定读。
在事务隔离级别已提交读(Read committed)、可重复读(Repeatable read InnoDB存储引擎默认的事务隔离级别)下，InnoDB存储引擎采用一致性非锁定读。

- 已提交读(Read committed)：每次普通的SELECT(非SELECT ... FOR UPDATE/SELECT ... LOCK IN SHARE MODE)都会读取数据的最新行版本（每次创建最新快照read view）。
- 可重复读(Repeatable read)：事务开启后第一次普通的SELECT(非SELECT ... FOR UPDATE/SELECT ... LOCK IN SHARE MODE)读取最新行版本（第一次创建快照，以后沿用read view）。













































