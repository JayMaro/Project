using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyMoce : MonoBehaviour
{
    
    Vector2 pos;
    public float delta;
    public float speed;
    // Start is called before the first frame update
    void Start()
    {
        
        pos = transform.position;
    }

    // Update is called once per frame
    void Update()
    {
        Vector2 v = pos;
        v.x += delta * Mathf.Sin(Time.time * speed);
        transform.position = v;

    }
   
}
