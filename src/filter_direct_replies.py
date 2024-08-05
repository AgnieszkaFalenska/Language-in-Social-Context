import json, bz2
import sys
import csv

def readTopics(topicsFile = "../data/cmv/topics.txt", topicsInfoFile = "../data/cmv/topics.info"):
    topicsInfo = { }
    for line in open(topicsInfoFile, "r"):
        tId, tInfo = line.strip().split(":")
        topicsInfo[tId] = "_".join(tInfo.split("_")[1:])

    topics = { }
    for line in open(topicsFile, "r"):
        cId, tId = line.strip().split()
        topics[cId] = topicsInfo[tId]

    return topics

if __name__ == '__main__':
    args = sys.argv[1:]
    dataFile = open(args[0], 'r')

    # read topics
    topicsInfo = args[1]
    topicsFile = args[2]
    topics = readTopics(topicsFile=topicsFile, topicsInfoFile=topicsInfo)

    outFile = open(args[3], "w")
    fieldnames = ['Author', 'Topic', 'Post', 'Replies']
    writer = csv.DictWriter(outFile, fieldnames=fieldnames)
    writer.writeheader()
    
    allExchanges = 0
    for line in dataFile:
        cmv  = json.loads(line)
        cmvId = cmv["id"]

        if cmvId not in topics:
            continue
        
        comments = cmv["comments"]
        
        authors = { cmvId : cmv["author"] }
        postTopics = { cmvId : topics[cmvId] }
        postTxts = { cmvId : " ".join(cmv["selftext"].split())}

        # read the comments tree
        children = {  }
        parents = { }
        for comment in comments:
            if "author" not in comment:
                continue

            cId = comment["id"]
            authors[cId] = comment["author"]
            postTxts[cId] = " ".join(comment["body"].split())
            postTopics[cId] = topics[cmvId]

            if cId not in children:
                children[cId] = [ ]

            if "replies" in comment and comment["replies"] and "data" in comment["replies"] and "children" in comment["replies"]["data"]:
                for childId in comment["replies"]["data"]["children"]:
                    children[cId].append(childId)
                    parents[childId] = cId

        children[cmvId] = [ cId for cId in children if cId not in parents ]
        
        
        # count exchanges
        exchange_pairs = { }
        for parentId, childrenIds in children.items():
            parentAuthor = authors[parentId]
            for childId in childrenIds:
                if childId not in authors:
                    continue

                childAuthor = authors[childId]
                authorPair = tuple(sorted([parentAuthor, childAuthor]))
                if authorPair not in exchange_pairs:
                    exchange_pairs[authorPair] = 1
                else:
                    exchange_pairs[authorPair] += 1

        # filter exchanges and store
        for parentId, childrenIds in children.items():
            parentAuthor = authors[parentId]

            row = {
                'Author': authors[parentId],
                'Post': postTxts[parentId],
                "Topic" : postTopics[parentId] }
             
            replies = [ ]
            for childId in childrenIds:
                if childId not in authors:
                    continue

                childAuthor = authors[childId]
                authorPair = tuple(sorted([parentAuthor, childAuthor]))
                if exchange_pairs[authorPair] < 5:
                    continue
            
                replies.append((authors[childId], postTxts[childId]))

            if len(replies) > 0:
                row["Replies"] = replies
                writer.writerow(row)
                allExchanges += len(replies)


    print("All exchanges", allExchanges)
            