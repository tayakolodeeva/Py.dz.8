def exp_pb(path, data):

    file_ = open(path,'w', encoding='UTF-8')

    for line in data:

        for e in line:

            file_.write(str(e) + '\n')

        file_.write('\n')

    file_.close