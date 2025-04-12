// 参考指令集如下，最后按需求统一调整格式
{
  "instruction" : "如何用C语言创建一个子进程？",
  "output" : "使用fork()系统调用，示例代码：\n#include <unistd.h>\npid_t pid = fork();\nif (pid == 0) { /* 子进程 */ }"
}

// file部分first_part的QA对已上传，目前仍存在重复，后续调整；  
// 下一步计划先生成file部分具体七部分（文件操作、权限管理、磁盘管理、文件搜索、压缩解压、文件系统类型、文件管理安全）的相关指令集
