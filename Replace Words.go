type Trie struct {
    is_word bool
    paths map[byte]*Trie
}

func NewTrie() *Trie {
    return &Trie{
        paths: make(map[byte]*Trie),
    }
}

func (t *Trie) Add(i int, word *string) {
    if i == len(*word) {
        t.is_word = true
        return
    }

    c := (*word)[i]
    if _, ok := t.paths[c]; !ok {
        t.paths[c] = NewTrie()
    }
    t.paths[c].Add(i+1, word)
}

func (t *Trie) Search(i int, word *string) string {
    if t.is_word {
        new_word := (*word)[:i]
        return new_word
    }

    if i == len(*word) {
        return *word
    }

    c := (*word)[i]
    if _, ok := t.paths[c]; !ok {
        return *word
    }

    return t.paths[c].Search(i+1, word)
}

func replaceWords(dictionary []string, sentence string) string {
    root := NewTrie()

    for _, word := range dictionary {
        root.Add(0, &word)
    }

    var ans strings.Builder
    splits := strings.Split(sentence, " ")
    for _, word := range splits {
        valid_word := root.Search(0, &word)
        ans.WriteString(valid_word)
        ans.WriteRune(' ')
    }

    ans_str := ans.String()
    return ans_str[:len(ans_str)-1]
}
