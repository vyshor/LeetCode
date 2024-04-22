type Node struct {
    val string
    steps int
    next *Node
}

var head *Node
var tail *Node

func popLeft() *Node {
    if head == nil {
        return nil
    }

    if head == tail {
        tail = nil
    }

    node := head
    head = head.next
    return node
}

func appendNode(node *Node) {
    if tail == nil {
        head = node
        tail = node
    } else {
        tail.next = node
        tail = node
    }
}

func openLock(deadends []string, target string) int {
    head = nil
    tail = nil

    if target == "0000" {
        return 0
    }

    visited := make(map[string]interface{})
    stuck := make(map[string]interface{})
    for _, deadend := range deadends {
        if deadend == "0000" {
            return -1
        }
        stuck[deadend] = nil
    }

    appendNode(&Node{
        val: "0000",
    })

    for tail != nil {
        node := popLeft()
        fmt.Println(node.val)
        num_str := node.val
        steps := node.steps
        steps += 1

        for i := 0; i < 4; i++ {
            for j := -1; j < 2; j += 2 {
                var new_num_str strings.Builder
                val := (int(num_str[i]) - '0' + j + 10) % 10
                new_num_str.WriteString(num_str[:i])
                new_num_str.WriteRune(rune('0' + val))
                new_num_str.WriteString(num_str[i+1:])
                new_str := new_num_str.String()


                if _, ok := visited[new_str]; ok {
                    continue
                }

                if _, ok := stuck[new_str]; ok {
                    continue
                }

                if new_str == target {
                    return steps
                }
                appendNode(&Node{
                    val: new_str,
                    steps: steps,
                })
                visited[new_str] = nil
            }
        }
    }
    return -1
}
