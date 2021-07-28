package org.acme;

import javax.enterprise.context.ApplicationScoped;
import javax.transaction.Transactional;
import javax.validation.Valid;
import java.util.List;
import java.util.Optional;

import static javax.transaction.Transactional.TxType.REQUIRED;
import static javax.transaction.Transactional.TxType.SUPPORTS;

@ApplicationScoped
@Transactional(REQUIRED)
public class TaskService {

    @Transactional(SUPPORTS)
    public List<TaskEntity> findAll() {
        return TaskEntity.listAll();
    }

    @Transactional(SUPPORTS)
    public Optional<TaskEntity> findById(Long id) {
        return TaskEntity.findByIdOptional(id);
    }

    public TaskEntity create(@Valid TaskEntity newEntity) {
        TaskEntity.persist(newEntity);
        return newEntity;
    }

    public TaskEntity update(@Valid TaskEntity newEntity) {
        TaskEntity oldEntity = TaskEntity.findById(newEntity.id);
        oldEntity.setName(newEntity.getName());
        oldEntity.setWayPoints(newEntity.getWayPoints());
        return oldEntity;
    }

    public void delete(Long id) {
        TaskEntity entity = TaskEntity.findById(id);
        entity.delete();
    }

}
