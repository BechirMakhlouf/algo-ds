package main

type Vertex struct {
	adjacent []*Vertex
	value    int
}

type Graph struct {
	vertices []*Vertex
	directed bool
}

func (g *Graph) addVertex(v *Vertex) error {
	g.vertices = append(g.vertices, v)
   
	return nil
}

func (g *Graph) addEdge(v *Vertex) error {
	return nil
}

func main() {
	var g Graph
	// var myGraph = map[int][]int {
	//   1: {1, 2, 3, 4, 5},
	// }
	//println("hello world")
	g.directed = false
  
	v := &Vertex{
		value: 5,
	}

	g.addVertex(v)

  myMap := make(map[int]bool)
  println("map: ", myMap[11])
  println("map: ", myMap[10])
  println("map: ", myMap[9])
  println("map: ", myMap[8])
}
