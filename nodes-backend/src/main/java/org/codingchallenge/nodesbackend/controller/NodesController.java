package org.codingchallenge.nodesbackend.controller;

import org.codingchallenge.nodesbackend.model.Node;
import org.codingchallenge.nodesbackend.repository.NodesRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.StreamSupport;

@RestController
public class NodesController {

    @Autowired
    NodesRepository nodesRepository;

    @GetMapping("/nodes")
    public List<Node> getAllNodes() {
        return StreamSupport.stream(nodesRepository.findAll().spliterator(), false)
                .distinct()
                .collect(Collectors.toList());
    }

    @PostMapping("/nodes")
    public Node saveNode(@RequestBody Node node) {
        return nodesRepository.save(node);
    }

    @GetMapping("/nodes/{nodeid}")
    public Node getNode(@PathVariable("nodeid") int nodeId) {
        return nodesRepository.findById(nodeId).get();
    }

    @DeleteMapping("/nodes")
    public void deleteAllNodes() {
        nodesRepository.deleteAll();
    }

    @DeleteMapping("/nodes/{nodeid}")
    public void deleteNode(@PathVariable("nodeid") int nodeId) {
        nodesRepository.deleteById(nodeId);
    }

    @PutMapping("/nodes")
    public Node updateNode(@RequestBody Node node) {
        return nodesRepository.save(node);
    }

}
