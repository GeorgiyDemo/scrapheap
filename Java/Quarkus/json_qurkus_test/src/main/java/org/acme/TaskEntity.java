package org.acme;


import com.vladmihalcea.hibernate.type.json.JsonBinaryType;
import io.quarkus.hibernate.orm.panache.PanacheEntity;
import lombok.Data;
import org.hibernate.annotations.Type;
import org.hibernate.annotations.TypeDef;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Table;
import javax.validation.constraints.NotNull;
import java.util.List;

@Data
@Entity
@Table(name = "tasks")
@TypeDef(name = "json", typeClass = JsonBinaryType.class)
public class TaskEntity extends PanacheEntity {

    @NotNull
    private String name;

    @Type(type = "json")
    @Column(columnDefinition = "json")
    @NotNull
    private List<WayPoint> wayPoints;

    @Override
    public String toString() {


        return "TaskEntity{" +
                "name='" + name + '\'' +
                ", wayPoints=" +
                '}';
    }
}
