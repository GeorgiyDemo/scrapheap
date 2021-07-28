package org.acme.services;

import org.acme.entities.UserEntity;

import javax.enterprise.context.ApplicationScoped;
import javax.transaction.Transactional;
import javax.validation.Valid;
import java.util.List;
import java.util.Optional;

import static javax.transaction.Transactional.TxType.REQUIRED;
import static javax.transaction.Transactional.TxType.SUPPORTS;

@ApplicationScoped
@Transactional(REQUIRED)
public class UserService {

    @Transactional(SUPPORTS)
    public List<UserEntity> findAll() {
        return UserEntity.listAll();
    }

    @Transactional(SUPPORTS)
    public Optional<UserEntity> findById(Long id) {
        return UserEntity.findByIdOptional(id);
    }

    public UserEntity create(@Valid UserEntity newEntity) {
        UserEntity.persist(newEntity);
        return newEntity;
    }

    public UserEntity update(@Valid UserEntity newEntity) {
        UserEntity oldEntity = UserEntity.findById(newEntity.id);
        oldEntity.setName(newEntity.getName());
        oldEntity.setTasks(newEntity.getTasks());
        return oldEntity;
    }

    public void delete(Long id) {
        UserEntity entity = UserEntity.findById(id);
        entity.delete();
    }

}
