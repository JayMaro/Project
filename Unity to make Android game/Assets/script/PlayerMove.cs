using JetBrains.Annotations;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PlayerMove : MonoBehaviour
{
    public AudioClip audioJump;
    public AudioClip audioDamaged;
    public AudioClip audioFinish;
    public Gamemanager gamemanager;
    public float W, H_s,H_b, X, Y_b,Y_b_s;
    public float maxSpeed;
    public float UpSpeed;
    public float Xspeed;
    public bool Aspect;
    public float JumpPower;
    private bool m_ladder;
    private bool inputJump = false;
    private bool inputDown = false;
    private bool But_on = false;


    Rigidbody2D rigid;
    SpriteRenderer spriteRenderer;
    Animator anim;
    BoxCollider2D  PlayerBox;
      
    AudioSource adS;
    

    void Start()
    {
        rigid = GetComponent<Rigidbody2D>();
        spriteRenderer = GetComponent<SpriteRenderer>();
        anim = GetComponent<Animator>();
        m_ladder = false;
        PlayerBox = GetComponent<BoxCollider2D>();
        
        adS = GetComponent<AudioSource>();
    }

    void Playsound(string action)
    {
        switch (action)
        {
            case "JUMP":
                adS.clip = audioJump;
                adS.Play();
                break;
            case "DAMAGED":
                adS.clip = audioDamaged;
                adS.Play();
                break;
            case "FINISH":
                adS.clip = audioFinish;
                adS.Play();
                break;
        }
    }
    void Update()
    {
        //Jump
        if (inputJump&& !anim.GetBool("isJumping")) {
            rigid.AddForce(Vector2.up * JumpPower, ForceMode2D.Impulse);
            anim.SetBool("isJumping", true);
            Playsound("JUMP");
            
        }

        //Stop Speed 
        if (!But_on)
        {
            rigid.velocity = new Vector2(0, rigid.velocity.y);
        }
        //Direction Sprite
        
        spriteRenderer.flipX = !Aspect;
           
        
        


        //animation
        if (rigid.velocity.normalized.x == 0)
            anim.SetBool("isWalking", false);                                

        else
            anim.SetBool("isWalking", true);
       
            

    }
    void FixedUpdate()
    {
        //Move By Key Control
        float h = Xspeed;
        //Move speed
        rigid.AddForce(Vector2.right * h, ForceMode2D.Impulse);
        

        if (rigid.velocity.x > maxSpeed)
            rigid.velocity = new Vector2(maxSpeed, rigid.velocity.y);
        else if (rigid.velocity.x < maxSpeed*(-1))
            rigid.velocity = new Vector2(maxSpeed*(-1), rigid.velocity.y);

        //Landing Platform
        if(rigid.velocity.y < 0)
        {
            Debug.DrawRay(rigid.position, Vector3.down, new Color(0, 1, 0));
            RaycastHit2D rayHit = Physics2D.Raycast(rigid.position, Vector3.down, 1, LayerMask.GetMask("Platform"));
            if (rayHit.collider != null)
            {
                if (rayHit.distance < 1.2f)
                    anim.SetBool("isJumping", false);

            }
        }
        //Down
        if (inputDown&& !inputJump)
        {
            anim.SetBool("isDown", true);
            rigid.velocity = new Vector2(0, rigid.velocity.y);
            if (PlayerBox != null)
            {
                PlayerBox.size = new Vector2(W, H_s);
                PlayerBox.offset = new Vector2(X, Y_b_s);
            }
        }
        else
            anim.SetBool("isDown", false);
        if (!inputDown)
        {
            anim.SetBool("isDown", false);
            if (PlayerBox != null)
            {
                PlayerBox.size = new Vector2(W, H_b);
                PlayerBox.offset = new Vector2(X, Y_b);
            }
        }
        



        //Ladder
        float UpDown ;
        UpDown = UpSpeed;
        if (m_ladder)
        {
            rigid.AddForce(Vector2.up * UpDown, ForceMode2D.Impulse);
            
            if (rigid.velocity.y > maxSpeed)
                rigid.velocity = new Vector2(rigid.velocity.x, maxSpeed);
            else if (rigid.velocity.y < maxSpeed * (-1))
                rigid.velocity = new Vector2(rigid.velocity.x, maxSpeed*(-1));
        }
       
       
    }

    void OnTriggerEnter2D(Collider2D Get)
    {
        if (Get.gameObject.tag.Equals("Ladder"))
        {
            if (!m_ladder)
            {
                m_ladder = true;
                anim.SetBool("isLadder", true);
                this.transform.Translate(0, 0.05f, 0);
            }
        }
        
       if(Get.gameObject.tag.Equals("End"))
        {
            //game clear
            Gamemanager.EndGame();
            Playsound("FINISH");
            Time.timeScale = 0;
           

        }
        
        
    }

    void OnTriggerExit2D(Collider2D Get)
    {
        if (Get.gameObject.tag.Equals("Ladder"))
        {
            if (m_ladder)
            {
                m_ladder = false;
                anim.SetBool("isLadder", false);
            }
        }
    }







    void OnCollisionEnter2D(Collision2D collision)
    {
        if(collision.gameObject.tag == "enemy")
        {
            OnDamaged(collision.transform.position);
        }
    }

    void OnDamaged(Vector2 targetPos)
    {
        //chage layer
        gameObject.layer = 14;
        //view alpha
        spriteRenderer.color = new Color(1, 1, 1, 0.4f);
        //reachtion force
        int dirc = transform.position.x - targetPos.x > 0 ? 1 : -1;
        rigid.AddForce(new Vector2(dirc, 1)*3, ForceMode2D.Impulse);
        //animation
        anim.SetTrigger("doDamaged");
        Playsound("DAMAGED");
        Invoke("OffDamaged", 0.7f);
        

    }

    void OffDamaged()
    {
        gameObject.layer = 9;
        spriteRenderer.color = new Color(1, 1, 1, 1);
    }

    public void JumpDown()
    {
        inputJump = true;
    }
    public void JumpUp()
    {
        inputJump = false;
    }
    public void Down_Up()
    {
        inputDown = false;
    }
    public void Down_Down()
    {
        inputDown = true;
    }

    public void Up_Down()
    {
       
        UpSpeed += 0.5f;
    }
    public void Up_Up()
    {
        
        UpSpeed -= 0.5f;
    }

    public void Right_Down()
    {
        But_on = true;
        Xspeed += 0.5f;
        Aspect = true;
    }
    public void Right_Up()
    {
        But_on = false;
        Xspeed -= 0.5f;
    }
    public void Left_Down()
    {
        But_on = true;
        Xspeed -= 0.5f;
        Aspect = false;
    }
    public void Left_Up()
    {
        But_on = false;
        Xspeed += 0.5f;
    }
}

