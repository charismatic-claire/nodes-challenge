package org.codingchallenge.nodesbackend.repository;

import org.codingchallenge.nodesbackend.model.Node;
import org.springframework.data.repository.CrudRepository;

public interface NodesRepository extends CrudRepository<Node, Integer> {

}
