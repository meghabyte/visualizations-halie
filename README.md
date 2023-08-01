# HALIE Visualizations

This site includes visualizations of interaction traces collected as part of HALIE ([Evaluating Human-Language Model Interaction](https://arxiv.org/abs/2212.09746)), with Stanford's Center for Research on Foundation Models. The raw data and source code for generating results are located in the [main HALIE repository](https://github.com/stanford-crfm/halie). These visualizations are intended to help viewers easily observe patterns and strategies of users interacting with different language models (LMs) when performing goal-oriented tasks. In particular, we currently provide visualizations for the following two tasks in HALIE: 

* **Question Answering**: An interactive version of a canonical NLP task (questio answering) where a user is asked to answer a question given access to an LM that they can query. In practice, users tend to query information systems repeatedly, refining and reformulating their queries in response to the system’s output.  
* **Crossword Puzzles**: A challenging task for AI systems which, unlike question answering, requires open-ended responses to often ambiguous clues (e.g. “Christmas in Chamonix”). The crossword puzzle task also provides additional structure, such as lexical constraints, which can influence user game-playing strategies and overall interaction behavior with an LM. 

In HALIE, users are provided one of the following four LMs to interact with: **Instruct-Davinci**, **Instruct-Babbage**, **Jumbo**, and **Davinci**. While these models are not as recent as ChatGPT and Claude, many of the observed interaction behaviors and patterns (such as detecting misinformation, accounting for model difficulty with numbers or logical reasoning) translate! 

For any questions, please contact [Megha Srivastava](https://cs.stanford.edu/~megha) (`megha@cs.stanford.edu`). 
