def generate_env_prompt():
    prompt = "You are an office assistant.\n"
    prompt += "### Office Environment ###\n"
    prompt += "There are some facilities like printer, vending machine, coffee machine, water dispenser, fridge, microwave. \n"
    prompt += "And there are some personal items like stapler: [fetch, deliver], scissors: [fetch, deliver], book: [fetch, deliver], data cable: [fetch, deliver], paper: [fetch, deliver], pen: [fetch, deliver], wipes: [fetch, deliver], seal: [fetch, deliver], document: [fetch, deliver, sign, seal], e-file[send, forward], cup[fetch, deliver]. Elements in [] means the instructions must contain one of these actions.  \n"
    prompt += "There are also some students like Mao, Sun, Lee, Zhang, Dang, Wang, Zhou, Chen, Yang, Hu, Lin, Gao, Xu, Zheng, Wu, Liu, Huang, He, Xue, Ren, Cai in the office. personal items belong to these students. \n"

    prompt += "### Rules ###\n"
    prompt += "Each student has 1-3 personal items. \n"
    prompt += "Each facility has at least 1 person to guard. \n"

    prompt += "Now you should distribute the personal items to all the students and guarding person to each facility.\n"
    prompt += "### Output format ###\n"
    prompt += "student:personal items\n"
    prompt += "facility:guarding person\n"

    prompt += "Here is an example1"
    prompt += "Mao: book, pen\n"
    prompt += "fridge: Sun\n"


    return prompt
def generate_ins_prompt(env):
    prompt = "You are an office assistant, you should generate some instructions.\n"
    prompt += "### Office Environment ###\n"
    prompt += "There are some facilities, personal items and students. \n"
    prompt += "The relation of personal items and guarding person is" + env
    prompt += "Students only have their personal items.\n"
    prompt += "Personal items:  stapler: [fetch, deliver], scissors: [fetch, deliver], book: [fetch, deliver], data cable: [fetch, deliver], paper: [fetch, deliver], pen: [fetch, deliver], wipes: [fetch, deliver], seal: [fetch, deliver], document: [fetch, deliver, sign, seal], e-file[send, forward]. Elements in [] means the instructions must contain one of these actions.  \n"
    prompt += "Facilities: printer[print(e-file), duplicate(document)], vending machine, coffee machine[get a cup of coffee(cup)], water dispenser[get a cup of water(cup)], fridge, microwave. Elements in [] means the instructions must contain one of these actions. Element in () is called accompaniment, which means if you want to do the actions in[], you must fetch the accompaniment from their owner first.\n"
    prompt += "### Rules ###\n"
    prompt += "Instructions must contain one origin which must be chosen in students or facilities. \n"
    # prompt += "Each facility has at least 1 person to guard which means if you want to use the facility you should inform that person. \n"
    prompt += "Particularly, action 'sign' and 'seal' must execute by a designated student.\n"
    prompt += "Now you should generate 10 instructions that students give you. Half of the instructions should contain 5 different facilities.\n"
    prompt += "### Output format ###\n"
    prompt += "JSON:{'origin': '', 'facility': [''], 'facility accompaniment': [''], 'personal item1': [''],'personal item2': ['']} instruction: \n"


    prompt += "Here are some examples\n"
    prompt += "JSON:{'origin': 'Mao', 'facility': ['printer'], 'facility accompaniment': document, 'personal item1': ['document'],'personal item2': null} instruction:Mao:Could fetch the document from Sun and duplicate it for me? \n"
    prompt += "JSON:{'origin': 'Lee', 'facility': null, 'facility accompaniment': null, 'personal item1': ['scissors'],'personal item2': null} instruction: Lee:Could you deliver me the scissors? \n"

    return prompt

def generate_miss_ins_prompt(env, ins):
    prompt = "You are an office assistant, you should rewrite some instructions.\n"
    prompt += "### Office Environment ###\n"
    prompt += "There are some facilities, personal items and students. \n"
    prompt += "The relation of personal items and guarding person is" + env
    prompt += "Students only have their personal items.\n"
    prompt += "Personal items:  stapler: [fetch, deliver], scissors: [fetch, deliver], book: [fetch, deliver], data cable: [fetch, deliver], paper: [fetch, deliver], pen: [fetch, deliver], wipes: [fetch, deliver], seal: [fetch, deliver], document: [fetch, deliver, sign, seal], e-file[send, forward]. Elements in [] means the instructions must contain one of these actions.  \n"
    prompt += "Facilities: printer[print(e-file), duplicate(document)], vending machine, coffee machine[get a cup of coffee(cup)], water dispenser[get a cup of water(cup)], fridge, microwave. Elements in [] means the instructions must contain one of these actions. Element in () is called accompaniment, which means if you want to use these facilties, you must have this element first.\n"
    prompt += "### Rules ###\n"
    # prompt += "Instructions must contain one origin, one destination, these place must be chosen in students or facilities. \n"
    # prompt += "Each facility has at least 1 person to guard which means if you want to use the facility you should inform that person. \n"

    prompt += "Here are some elements in json format and 10 instructions based on the 10 jsons:\n" + ins
    prompt += "Now you should rewrite the 10 instructions that miss one element in the relevant jsons to make them unclear.\n"
    prompt += "You can only miss one element from 'facility accompaniment' , owner of facility accompaniment and the student who will sign or seal a document.\n"
    prompt += "Personal item, facility and relevant actions must be clear.\n"

    prompt += "### Output format ###\n"
    prompt += "Unclear instruction: \n"

    prompt += "Here are some examples"
    prompt += "Input instruction: Could you deliver this document for Mao to sign?\n"
    prompt += "Unclear instruction: Could you deliver this document to sign?\n"
    prompt += "Input instruction: Could you fetch the document from Mao and duplicate it?\n"
    prompt += "Unclear instruction: Could you fetch the document and duplicate it?\n"
    # prompt += "JSON:{'origin': 'Mao', 'destination': 'Mao', 'facility1': ['water dispenser'], 'facility2': null, 'personal item1': [' cup'],'personal item2': null} instruction:Mao:Could you send me a cup of water? \n"
    # prompt += "JSON:{'origin': 'Lee', 'destination': 'Zhang', 'facility1': null, 'facility2': null, 'personal item1': ['scissors'],'personal item2': null} instruction: Lee:Could you deliver me the scissors from  Zhang? \n"

    return prompt
def generate_clarify_prompt(env,miss_ins):
    prompt = "You are a clarify assistant, you should generate some clarify answer.\n"
    prompt += "### Office Environment ###\n"
    prompt += "There are some facilities, personal items and students. \n"
    prompt += "The relation of personal items and guarding person is" + env
    prompt += "Students only have their personal items."
    prompt += "Personal items:  stapler: [fetch, deliver], scissors: [fetch, deliver], book: [fetch, deliver], data cable: [fetch, deliver], paper: [fetch, deliver], pen: [fetch, deliver], wipes: [fetch, deliver], seal: [fetch, deliver], document: [fetch, deliver, sign, seal], e-file[send, forward]. Elements in [] means the instructions must contain one of these actions.  \n"
    prompt += "Facilities: printer[print(e-file), duplicate(document)], vending machine, coffee machine[get a cup of coffee(cup)], water dispenser[get a cup of water(cup)], fridge, microwave. Elements in [] means the instructions must contain one of these actions. Element in () is called accompaniment, which means if you want to use these facilties, you must have this element first.\n"
    prompt += "### Rules ###\n"
    prompt += "Instructions must contain one origin which must be chosen in students or facilities. \n"
    # prompt += "Each facility has at least 1 person to guard which means if you want to use the facility you should inform that person. \n"
    prompt += "If the instruction miss the owner of the personal item, but the action is not seal or sign, you should not clarify the owner.\n"
    prompt += "Particularly, action 'sign' and 'seal' must execute by a designated student. If the instruction include 'sign' or 'seal' but miss the designated student, the clarify question should ask about it.\n"
    prompt += "If the instruction miss the facility accompaniment, or the owner of it, you should ask about it.\n"
    prompt += "Here are 10 unclear instructions:" + miss_ins
    prompt += "Now you should generate 10 clarify questions based on the 10 unclear instructions to ask the user.\n"
    prompt += "### Output format ###\n"
    prompt += "Unclear instruction: \n"
    prompt += "Clarify question: \n"

    prompt += "Here are some examples"
    prompt += "unclear instruction: Could you fetch the document and duplicate it for me?\n"
    prompt += "clarify answer: Could you specify which place should I get the document?\n"

    return prompt