import React from "react";
import {AppBar, Toolbar, Typography, Button, 
        IconButton, InputBase, fade, makeStyles} from "@material-ui/core";
import SearchIcon from "@material-ui/icons/Search";
import { FaClipboard } from "react-icons/fa";
import { MdForum } from "react-icons/md";
import { SiEthereum } from "react-icons/si";
import { useHistory } from "react-router-dom";
import { useDispatch } from "react-redux";
import Avatar from '@material-ui/core/Avatar';
import MenuIcon from "@material-ui/icons/Menu";
import CheckWeb3 from "../Blockchain/Web3Utils";
import { lightTheme, darkTheme } from '../Themes/Theme';


const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },

  menuButton: {
    color:'inherit',
    marginRight: theme.spacing(1),
  },

  title: {
    flexGrow: 1,
    display: "none",
    [theme.breakpoints.up("sm")]: {
      display: "block",
    },
  },

  titleButton: {
    color:'inherit',
    fontSize: '18px',
    marginLeft: theme.spacing(-1),
  },

  search: {
    position: 'relative',
    borderRadius: theme.shape.borderRadius,
    backgroundColor: fade(theme.palette.common.white, 0.15),
    '&:hover': {
      backgroundColor: fade(theme.palette.common.white, 0.25),
    },
    marginRight: theme.spacing(39.5),
    marginLeft: 0,
    width: '100%',
    [theme.breakpoints.up('sm')]: {
      marginLeft: theme.spacing(3),
      width: '580px', /*auto*/
    },
  },

  searchIcon: {
    padding: theme.spacing(0, 2),
    height: '100%',
    position: 'absolute',
    pointerEvents: 'none',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },

  inputRoot: {
    color: 'inherit',
  },

  inputInput: {
    padding: theme.spacing(1, 1, 1, 0),
    // vertical padding + font size from searchIcon
    paddingLeft: `calc(1em + ${theme.spacing(4)}px)`,
    transition: theme.transitions.create('width'),
    width: '100%',
    [theme.breakpoints.up('md')]: {
      width: '20ch',
    },
  },

  button:{
    color: 'inherit',
  },

  loginButton: {
    color: 'inherit',
    backgroundColor: fade(theme.palette.common.white, 0.15),
    '&:hover': {
      backgroundColor: fade(theme.palette.common.white, 0.25),
    },
    textTransform: 'none',
    alignItems: 'center',
    justifyContent: 'center',
    width: '80px',
    height: '32px',
    marginRight: theme.spacing(1),
    // marginleft: theme.spacing(1),
  }, 

  iconButton: {
    color: 'inherit',
    marginRight: theme.spacing(1),
  },

  avatar: {
    width: '38px',
    height: '38px',
  },
}));


export default function TopBar(props) {
  const classes = useStyles();
  const history = useHistory();
  const dispatch = useDispatch();
  const searchAll = (text) => {};

  return (
    <div className={classes.root}>
      <AppBar position="fixed" fixed='top' style={{ zindex: 1, backgroundColor: "#18181b"}}>
        <Toolbar variant="dense">
          <IconButton
            edge="start"
            className={classes.menuButton}
            aria-label="open drawer"
            disableRipple
          >
            <MenuIcon />
          </IconButton>
          
          <Typography className={classes.title} variant="h6" noWrap>
            <IconButton disableRipple onClick={() => history.push("/")} className={classes.titleButton}>
                Shadder
            </IconButton>           
          </Typography>         

          <div className={classes.search}>
            <div className={classes.searchIcon}>
              <SearchIcon />
            </div>
            <InputBase
              placeholder="Search"
              classes={{
                root: classes.inputRoot,
                input: classes.inputInput,
              }}
              // onChange={(e) => searchAll(e.target.value)}
              inputProps={{ "aria-label": "search" }}
            />
          </div>
          <div className={classes.grow} />
          {/* <IconButton
            onClick={() => history.push("/")}
            aria-label="home page"
            disableRipple
            className={classes.iconButton}
          >
            <HomeIcon />
          </IconButton> */}
          
          <IconButton disableRipple onClick={() => history.push("/threads")} className={classes.iconButton}>
            <MdForum />
          </IconButton>

          <IconButton disableRipple onClick={() => history.push("/boards")} className={classes.iconButton}>
            <FaClipboard />
          </IconButton>     
          
          <IconButton disableRipple onClick={() => CheckWeb3()} className={classes.iconButton}>
            <SiEthereum />
          </IconButton>

          {/* TODO: implement Sign Up */}
          {/* {props.isAuthenticated ? null
            : <Button disableRipple onClick={() => history.push("/sign_up")} className={classes.button}>
                Sign Up
              </Button>
          } */}
          
          {/* TODO: implement Password Update */}
          {/* {props.isAuthenticated ? (
            <Button disableRipple onClick={() => history.push("/password_update")} className={classes.button}>
              Update Password
            </Button>
          ) : null} */}

          {props.isAuthenticated ? (
            <Button variant="contained" onClick={() => props.logout()} className={classes.loginButton} >
              Logout
            </Button>
           ) : 
            <Button variant="contained" onClick={() => history.push("/login")} className={classes.loginButton}>
              Log In
            </Button>
          }

          <div>
            <Button disableRipple className={classes.button}>
              <Avatar className={classes.avatar} src={process.env.PUBLIC_URL + '/defAvatar.jpg'}/>
            </Button>              
          </div>

        </Toolbar>
      </AppBar>
    </div>
  );
}
