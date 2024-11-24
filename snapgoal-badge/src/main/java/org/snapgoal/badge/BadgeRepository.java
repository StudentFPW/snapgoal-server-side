package org.snapgoal.badge;

import org.springframework.data.repository.CrudRepository;

import org.snapgoal.badge.Badge;

// This will be AUTO IMPLEMENTED by Spring into a Bean called badgeRepository
// CRUD refers Create, Read, Update, Delete

public interface BadgeRepository extends CrudRepository<Badge, Integer> {

}
