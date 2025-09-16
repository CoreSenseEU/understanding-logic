
cnf(vector_to_triple_engine, axiom,
  ~k(X, vector, vector3_msg) |
  k(exert1(vector_to_triple_engine, vector3_msg), triple, triple_msg)
).

cnf(point_to_triple_engine, axiom,
  ~k(X, point, point_msg) |
  k(exert1(point_to_triple_engine, point_msg), triple, triple_msg)
).

cnf(triple_to_vector_engine, axiom,
  ~k(X, triple, triple_msg) |
  k(exert1(triple_to_vector_engine, triple_msg), vector, vector3_msg)
).

cnf(triple_to_point_engine, axiom,
  ~k(X, triple, triple_msg) |
  k(exert1(triple_to_point_engine, triple_msg), point, point_msg)
).

cnf(imu0_modelet,axiom,
    k(init(imu0_modelet),inertia,imu_msg)
).
cnf(gnss0_modelet,axiom,
    k(init(gnss0_modelet),geolocation,navSatFix_msg)
).
cnf(rotor_force0_modelet,axiom,
    k(init(rotor_force0_modelet),force,vector3_msg)
).
cnf(trajectory0_modelet,axiom,
    k(init(trajectory0_modelet),trajectory,vector3_msg)
).
cnf(wind0_modelet,axiom,
    k(init(wind0_modelet),wind,vector3_msg)
).

cnf(dse_engine,axiom,~k(X,geolocation,navSatFix_msg) |
                     ~k(Y,inertia,imu_msg) |
                     k(exert2(dse_engine,X,Y),drone_state,drone_state_msg)
).

cnf(dsee_engine,axiom,~k(X,drone_state,drone_state_msg) |
                      ~k(Y,wind,vector3_msg) |
                      ~k(Z,trajectory,vector3_msg) |
                      k(exert3(dsee_engine,X,Y,Z),drone_state_evolution,drone_state_evolution_msg)
).

cnf(we_engine,axiom,~k(X,drone_state,drone_state_msg) |
                    ~k(Y,drone_state_evolution,drone_state_evolution_msg) |
                    k(exert2(we_engine,X,Y),wind,vector3_msg)
).

fof(q,question,?[X]:k(X,drone_state_evolution,drone_state_evolution_msg)).
