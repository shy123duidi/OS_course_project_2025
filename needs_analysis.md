# 需求分析 needs_analysis
# 要求详细描述项目的功能需求和设计目标
1.功能需求

2.设计目标

# 后续安排及基本流程设计
1.训练模型数据准备：自行构建操作系统领域数据集  
  可能参考的相关文本：Linux手册页(man pages)、内核文档、清华github上的os-lectures、OS课程PPT等  
  构建指令数据集：instruction \ output  
2.模型微调  
  Hugging Face Transfomers库，基于LoRA微调，适配OS领域知识  
  优化相关提示词模板：如(加入角色设定：“你是一个操作系统领域的专家...”)
3.评估  
  设计测试用例：测试命令正确性、代码可编译性等  
  进行微调前后的对比实验  
4.部署前端交互    
  开发Gradio/Streamlit网页界面或命令行工具(Python + 'argparse')
